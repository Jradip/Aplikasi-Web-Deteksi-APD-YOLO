from __future__ import annotations

import threading
import time
from pathlib import Path
from textwrap import dedent
from typing import Optional

import av
import streamlit as st
import streamlit.components.v1 as components
from streamlit_webrtc import (
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)

from styles import CUSTOM_CSS
import icons


# ============================================================
# Konfigurasi
# ============================================================

MODEL_DIR = Path("models")

YOLO11_MODEL = MODEL_DIR / "YOLO11s_APD_best.pt"
FALLBACK_MODEL = MODEL_DIR / "best.pt"

DEFAULT_IMAGE_SIZE = 320
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 360
CAMERA_FPS = 15
MAX_DETECTIONS = 30

PRIMARY_COLOR = "#0EA5A4"
WHITE_COLOR = "#FFFFFF"

CLASS_CARDS = [
    ("Pekerja", "person", icons.icon_shield),
    ("Helm", "helmet", icons.icon_helmet),
    ("Rompi", "vest", icons.icon_vest),
]

CLASS_LABEL_MAP = {
    "person": "Pekerja",
    "pekerja": "Pekerja",
    "worker": "Pekerja",

    "helmet": "Helm",
    "helm": "Helm",
    "hardhat": "Helm",
    "helm keselamatan": "Helm",

    "vest": "Rompi",
    "rompi": "Rompi",
    "safety vest": "Rompi",
    "rompi keselamatan": "Rompi",
}


# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="APD Detection — YOLO11 Realtime Monitor",
    page_icon="⛑️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# Helper HTML
# ============================================================

def clean_html(markup: str) -> str:
    return " ".join(
        line.strip()
        for line in dedent(markup).strip().splitlines()
        if line.strip()
    )


def html(markup: str):
    st.markdown(clean_html(markup), unsafe_allow_html=True)


def slot_html(slot, markup: str):
    slot.markdown(clean_html(markup), unsafe_allow_html=True)


# ============================================================
# Styling khusus iframe streamlit-webrtc
# ============================================================

def inject_webrtc_control_style():
    components.html(
        """
        <script>
        (function () {
            function getText(el) {
                return (el.innerText || el.textContent || "").trim().toUpperCase();
            }

            function commonAncestor(a, b) {
                if (!a) return b || null;
                if (!b) return a || null;

                const parents = new Set();
                let node = a;

                while (node) {
                    parents.add(node);
                    node = node.parentElement;
                }

                node = b;

                while (node) {
                    if (parents.has(node)) return node;
                    node = node.parentElement;
                }

                return a.parentElement;
            }

            function unlockParentScroll() {
                try {
                    const pdoc = window.parent.document;

                    pdoc.documentElement.style.overflowY = "auto";
                    pdoc.documentElement.style.overflowX = "hidden";
                    pdoc.documentElement.style.height = "auto";
                    pdoc.documentElement.style.maxHeight = "none";

                    pdoc.body.style.overflowY = "auto";
                    pdoc.body.style.overflowX = "hidden";
                    pdoc.body.style.height = "auto";
                    pdoc.body.style.maxHeight = "none";

                    const app = pdoc.querySelector(".stApp");
                    if (app) {
                        app.style.overflowY = "auto";
                        app.style.height = "auto";
                        app.style.maxHeight = "none";
                    }

                    const appView = pdoc.querySelector("[data-testid='stAppViewContainer']");
                    if (appView) {
                        appView.style.overflowY = "auto";
                        appView.style.height = "auto";
                        appView.style.maxHeight = "none";
                    }

                    const main = pdoc.querySelector("[data-testid='stMain'], main");
                    if (main) {
                        main.style.overflowY = "visible";
                        main.style.height = "auto";
                        main.style.maxHeight = "none";
                    }

                    const block = pdoc.querySelector(".block-container");
                    if (block) {
                        block.style.overflow = "visible";
                        block.style.height = "auto";
                        block.style.maxHeight = "none";
                    }
                } catch (error) {
                    // Abaikan jika browser membatasi akses parent.
                }
            }

            function findControlBar(doc, startButton, selectButton) {
                const bodyWidth = doc.body.getBoundingClientRect().width || 900;
                const targets = [startButton, selectButton].filter(Boolean);
                const nodes = Array.from(doc.querySelectorAll("div, section, main, footer"));

                const candidates = nodes
                    .filter((node) => {
                        const rect = node.getBoundingClientRect();
                        const containsButtons = targets.every((target) => node.contains(target));

                        return (
                            containsButtons &&
                            rect.width >= bodyWidth * 0.65 &&
                            rect.height >= 28 &&
                            rect.height <= 130
                        );
                    })
                    .map((node) => {
                        const rect = node.getBoundingClientRect();
                        return {
                            node: node,
                            area: rect.width * rect.height,
                        };
                    })
                    .sort((a, b) => a.area - b.area);

                if (candidates.length > 0) {
                    return candidates[0].node;
                }

                return commonAncestor(startButton, selectButton);
            }

            function styleButton(button, type) {
                button.style.boxSizing = "border-box";
                button.style.fontFamily = "Inter, Arial, sans-serif";
                button.style.transition = "all 0.18s ease";
                button.style.borderRadius = "12px";
                button.style.fontWeight = "850";
                button.style.fontSize = "13px";
                button.style.height = "34px";
                button.style.minHeight = "34px";
                button.style.lineHeight = "1";
                button.style.padding = "0 18px";
                button.style.margin = "0";
                button.style.display = "inline-flex";
                button.style.alignItems = "center";
                button.style.justifyContent = "center";
                button.style.letterSpacing = "0.01em";
                button.style.whiteSpace = "nowrap";
                button.style.transform = "none";

                if (type === "start") {
                    button.style.minWidth = "96px";
                    button.style.background = "linear-gradient(135deg, #0EA5A4 0%, #0F766E 100%)";
                    button.style.border = "1px solid rgba(15, 118, 110, 0.75)";
                    button.style.color = "#FFFFFF";
                    button.style.boxShadow = "0 6px 14px rgba(14, 165, 164, 0.20)";
                }

                if (type === "stop") {
                    button.style.minWidth = "96px";
                    button.style.background = "linear-gradient(135deg, #EF4444 0%, #B91C1C 100%)";
                    button.style.border = "1px solid rgba(185, 28, 28, 0.75)";
                    button.style.color = "#FFFFFF";
                    button.style.boxShadow = "0 6px 14px rgba(239, 68, 68, 0.18)";
                }

                if (type === "select") {
                    button.style.minWidth = "160px";
                    button.style.background = "#FFFFFF";
                    button.style.border = "1px solid rgba(148, 163, 184, 0.65)";
                    button.style.color = "#0F172A";
                    button.style.boxShadow = "0 6px 14px rgba(15, 23, 42, 0.06)";
                }

                if (type === "done") {
                    button.style.minWidth = "96px";
                    button.style.background = "linear-gradient(135deg, #0EA5A4 0%, #0F766E 100%)";
                    button.style.border = "1px solid rgba(15, 118, 110, 0.75)";
                    button.style.color = "#FFFFFF";
                    button.style.boxShadow = "0 7px 16px rgba(14, 165, 164, 0.22)";
                }
            }

            function setOuterFrame(frame, height) {
                frame.style.width = "100%";
                frame.style.height = height + "px";
                frame.style.minHeight = height + "px";
                frame.style.maxHeight = height + "px";
                frame.style.border = "none";
                frame.style.borderRadius = "20px";
                frame.style.display = "block";
                frame.style.background = "#FFFFFF";
                frame.style.overflow = "hidden";
                frame.setAttribute("height", String(height));

                const wrapper = frame.parentElement;

                if (wrapper) {
                    wrapper.style.height = height + "px";
                    wrapper.style.minHeight = height + "px";
                    wrapper.style.maxHeight = height + "px";
                    wrapper.style.background = "#FFFFFF";
                    wrapper.style.border = "1px solid #C7DCE8";
                    wrapper.style.borderRadius = "20px";
                    wrapper.style.boxShadow = "0 14px 32px rgba(15, 23, 42, 0.07)";
                    wrapper.style.padding = "0";
                    wrapper.style.marginTop = "0.75rem";
                    wrapper.style.marginBottom = "1rem";
                    wrapper.style.overflow = "hidden";
                    wrapper.style.boxSizing = "border-box";
                    wrapper.style.lineHeight = "0";
                }
            }

            function stylePreviewArea(doc, video, controlBar, previewHeight) {
                const mediaElements = Array.from(doc.querySelectorAll("video, canvas"));

                mediaElements.forEach((el) => {
                    if (controlBar && controlBar.contains(el)) return;

                    el.style.width = "100%";
                    el.style.height = previewHeight + "px";
                    el.style.minHeight = previewHeight + "px";
                    el.style.maxHeight = previewHeight + "px";
                    el.style.objectFit = "contain";
                    el.style.display = "block";
                    el.style.background = "#EDF3F6";
                    el.style.borderRadius = "20px 20px 0 0";
                    el.style.margin = "0";

                    if (el.tagName === "VIDEO") {
                        el.controls = false;
                        el.removeAttribute("controls");
                        el.playsInline = true;
                    }
                });

                if (video) {
                    let node = video.parentElement;
                    let depth = 0;

                    while (node && node !== doc.body && depth < 5) {
                        if (controlBar && node.contains(controlBar)) break;

                        node.style.width = "100%";
                        node.style.height = previewHeight + "px";
                        node.style.minHeight = previewHeight + "px";
                        node.style.maxHeight = previewHeight + "px";
                        node.style.overflow = "hidden";
                        node.style.background = "#EDF3F6";
                        node.style.margin = "0";
                        node.style.padding = "0";
                        node.style.borderRadius = "20px 20px 0 0";
                        node.style.boxSizing = "border-box";

                        node = node.parentElement;
                        depth += 1;
                    }
                }
            }

            function styleDeviceSelector(doc, frame) {
                const frameHeight = 210;

                setOuterFrame(frame, frameHeight);

                doc.documentElement.style.margin = "0";
                doc.documentElement.style.padding = "0";
                doc.documentElement.style.width = "100%";
                doc.documentElement.style.height = frameHeight + "px";
                doc.documentElement.style.background = "#FFFFFF";
                doc.documentElement.style.overflow = "hidden";

                doc.body.style.margin = "0";
                doc.body.style.padding = "14px 18px";
                doc.body.style.width = "100%";
                doc.body.style.height = frameHeight + "px";
                doc.body.style.background = "linear-gradient(135deg, #FFFFFF 0%, #F7FCFD 100%)";
                doc.body.style.overflow = "hidden";
                doc.body.style.fontFamily = "Inter, Arial, sans-serif";
                doc.body.style.position = "relative";
                doc.body.style.boxSizing = "border-box";

                const video = doc.querySelector("video");

                if (video) {
                    video.style.width = "168px";
                    video.style.height = "118px";
                    video.style.objectFit = "cover";
                    video.style.borderRadius = "15px";
                    video.style.border = "1px solid #C7DCE8";
                    video.style.boxShadow = "0 10px 22px rgba(15, 23, 42, 0.10)";
                    video.style.background = "#FFFFFF";
                    video.style.display = "block";
                    video.style.margin = "0";
                }

                const selects = Array.from(doc.querySelectorAll("select"));

                selects.forEach((select) => {
                    select.style.width = "100%";
                    select.style.maxWidth = "420px";
                    select.style.height = "42px";
                    select.style.borderRadius = "12px";
                    select.style.border = "1px solid #CBD5E1";
                    select.style.background = "#FFFFFF";
                    select.style.color = "#0F172A";
                    select.style.padding = "0 14px";
                    select.style.fontSize = "14px";
                    select.style.fontWeight = "700";
                    select.style.boxShadow = "0 8px 18px rgba(15, 23, 42, 0.06)";
                    select.style.outline = "none";
                });

                Array.from(doc.querySelectorAll("label, span, p, div")).forEach((el) => {
                    const text = getText(el);

                    if (text === "VIDEO INPUT") {
                        el.style.color = "#0F766E";
                        el.style.fontSize = "11px";
                        el.style.fontWeight = "900";
                        el.style.letterSpacing = "0.12em";
                        el.style.textTransform = "uppercase";
                        el.style.marginBottom = "7px";
                    }
                });

                Array.from(doc.querySelectorAll("button")).forEach((button) => {
                    const text = getText(button);

                    if (text.includes("DONE")) {
                        styleButton(button, "done");
                        button.style.position = "absolute";
                        button.style.left = "18px";
                        button.style.bottom = "14px";
                        button.style.zIndex = "20";
                    }
                });
            }

            function applyWebRTCStyle() {
                unlockParentScroll();

                const frames = window.parent.document.querySelectorAll("iframe");

                frames.forEach((frame) => {
                    try {
                        const doc = frame.contentDocument || frame.contentWindow.document;
                        if (!doc || !doc.body) return;

                        const buttons = Array.from(doc.querySelectorAll("button"));
                        if (!buttons.length) return;

                        let startButton = null;
                        let selectButton = null;
                        let doneButton = null;

                        buttons.forEach((button) => {
                            const text = getText(button);

                            if (text.includes("START")) {
                                startButton = button;
                                styleButton(button, "start");
                            }

                            if (text.includes("STOP")) {
                                startButton = button;
                                styleButton(button, "stop");
                            }

                            if (text.includes("SELECT DEVICE")) {
                                selectButton = button;
                                styleButton(button, "select");
                            }

                            if (text.includes("DONE")) {
                                doneButton = button;
                                styleButton(button, "done");
                            }
                        });

                        const bodyText = getText(doc.body);
                        const isDeviceSelector =
                            bodyText.includes("VIDEO INPUT") ||
                            bodyText.includes("AUDIO INPUT") ||
                            doneButton !== null;

                        if (isDeviceSelector) {
                            styleDeviceSelector(doc, frame);
                            return;
                        }

                        if (!startButton && !selectButton) return;

                        const video = doc.querySelector("video");
                        const videoActive = video && video.videoWidth > 0;

                        const controlBar = findControlBar(doc, startButton, selectButton);
                        const controlHeight = 54;

                        const frameWidth = frame.getBoundingClientRect().width || 900;
                        const sourceAspect =
                            videoActive && video.videoWidth > 0
                                ? video.videoHeight / video.videoWidth
                                : 9 / 16;
                        const activePreviewHeight = Math.max(
                            480,
                            Math.min(860, Math.round(frameWidth * sourceAspect))
                        );
                        const standbyPreviewHeight = 120;

                        const previewHeight = videoActive ? activePreviewHeight : standbyPreviewHeight;
                        const frameHeight = previewHeight + controlHeight;

                        doc.documentElement.style.margin = "0";
                        doc.documentElement.style.padding = "0";
                        doc.documentElement.style.width = "100%";
                        doc.documentElement.style.height = frameHeight + "px";
                        doc.documentElement.style.background = "#FFFFFF";
                        doc.documentElement.style.overflow = "hidden";

                        doc.body.style.margin = "0";
                        doc.body.style.padding = "0";
                        doc.body.style.width = "100%";
                        doc.body.style.height = frameHeight + "px";
                        doc.body.style.background = "#FFFFFF";
                        doc.body.style.overflow = "hidden";
                        doc.body.style.fontFamily = "Inter, Arial, sans-serif";
                        doc.body.style.position = "relative";
                        doc.body.style.boxSizing = "border-box";

                        setOuterFrame(frame, frameHeight);

                        if (controlBar) {
                            controlBar.style.width = "100%";
                            controlBar.style.height = controlHeight + "px";
                            controlBar.style.minHeight = controlHeight + "px";
                            controlBar.style.maxHeight = controlHeight + "px";
                            controlBar.style.padding = "9px 14px";
                            controlBar.style.margin = "0";
                            controlBar.style.boxSizing = "border-box";
                            controlBar.style.display = "flex";
                            controlBar.style.alignItems = "center";
                            controlBar.style.justifyContent = "space-between";
                            controlBar.style.gap = "12px";
                            controlBar.style.background = "linear-gradient(90deg, #DDF7F4 0%, #EAF3FF 100%)";
                            controlBar.style.border = "none";
                            controlBar.style.borderTop = "1px solid #C6DCE8";
                            controlBar.style.borderRadius = "0 0 20px 20px";
                            controlBar.style.boxShadow = "inset 0 1px 0 rgba(255,255,255,0.75)";
                            controlBar.style.overflow = "visible";
                            controlBar.style.position = "absolute";
                            controlBar.style.left = "0";
                            controlBar.style.right = "0";
                            controlBar.style.bottom = "0";
                            controlBar.style.zIndex = "50";
                        }

                        stylePreviewArea(doc, video, controlBar, previewHeight);

                    } catch (error) {
                        // Abaikan iframe yang tidak bisa diakses.
                    }
                });
            }

            applyWebRTCStyle();
            setInterval(applyWebRTCStyle, 500);
        })();
        </script>
        """,
        height=0,
        width=0,
    )


st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ============================================================
# Session State
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "landing"


def goto(page: str):
    st.session_state.page = page


# ============================================================
# Helper Model
# ============================================================

def find_model() -> Optional[Path]:
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if YOLO11_MODEL.exists():
        return YOLO11_MODEL

    if FALLBACK_MODEL.exists():
        return FALLBACK_MODEL

    model_files = sorted(MODEL_DIR.glob("*.pt"))

    if model_files:
        return model_files[0]

    return None


@st.cache_resource(show_spinner="Memuat model YOLO...")
def load_model(model_path: str):
    from ultralytics import YOLO

    return YOLO(model_path)


def normalize_label(label: str) -> str:
    key = str(label).strip().lower()
    return CLASS_LABEL_MAP.get(key, label)


def get_class_name(names, class_id: int) -> str:
    if isinstance(names, dict):
        raw_name = names.get(class_id, str(class_id))
    elif isinstance(names, list) and class_id < len(names):
        raw_name = names[class_id]
    else:
        raw_name = str(class_id)

    return normalize_label(raw_name)


def color_for_label(label: str) -> str:
    label_lower = label.lower()

    if "tanpa" in label_lower or "no-" in label_lower or "not" in label_lower:
        return "#EF4444"

    return "#16A34A"


def summarize_counter(counter: dict) -> str:
    if not counter:
        return "Belum ada objek terdeteksi."

    return " · ".join([f"{name}: {count}" for name, count in counter.items()])


# ============================================================
# Top Navigation
# ============================================================

def render_top_navigation():
    with st.container(key="top_navigation"):
        brand_col, landing_col, detect_col = st.columns(
            [4.6, 1.15, 1.55],
            vertical_alignment="center",
            gap="small",
        )

        with brand_col:
            html(
                f"""
                <div class="top-brand">
                    <span class="top-brand-mark">{icons.icon_shield(21, WHITE_COLOR)}</span>
                    <span>
                        <strong>APD Detection</strong>
                        <small>YOLO11 Realtime Monitor</small>
                    </span>
                </div>
                """
            )

        with landing_col:
            st.button(
                "Beranda",
                key="top_nav_landing",
                type="primary" if st.session_state.page == "landing" else "tertiary",
                use_container_width=True,
                on_click=goto,
                args=("landing",),
            )

        with detect_col:
            st.button(
                "Deteksi Webcam",
                key="top_nav_detect",
                type="primary" if st.session_state.page == "detect" else "tertiary",
                use_container_width=True,
                on_click=goto,
                args=("detect",),
            )


def render_detection_configuration(model_path: Optional[Path]):
    model_name = model_path.name if model_path is not None else "Model belum tersedia"
    display_model_name = model_name.replace("YOLOv11", "YOLO11")
    model_state = "Model siap" if model_path is not None else "Model belum tersedia"
    model_state_class = "ready" if model_path is not None else "missing"

    html(
        f"""
        <div class="configuration-heading">
            <div>
                <div class="configuration-kicker">Konfigurasi Pengujian</div>
                <h3>Siapkan model dan parameter deteksi</h3>
                <p>Periksa sumber kamera dan sesuaikan parameter sebelum memulai pemantauan realtime.</p>
            </div>
            <div class="configuration-state {model_state_class}">
                <span></span>{model_state}
            </div>
        </div>
        <div class="deployment-grid">
            <div class="deployment-item">
                <div class="deployment-icon">{icons.icon_shield(19, PRIMARY_COLOR)}</div>
                <div>
                    <span>Model aktif</span>
                    <strong>{display_model_name}</strong>
                    <small>YOLO11 · Object Detection</small>
                </div>
            </div>
            <div class="deployment-item">
                <div class="deployment-icon">{icons.icon_camera(19, PRIMARY_COLOR)}</div>
                <div>
                    <span>Sumber input</span>
                    <strong>Webcam Browser</strong>
                    <small>Video realtime tanpa audio</small>
                </div>
            </div>
            <div class="deployment-item">
                <div class="deployment-icon">{icons.icon_gauge(19, PRIMARY_COLOR)}</div>
                <div>
                    <span>Mode pemrosesan</span>
                    <strong>Realtime Inference</strong>
                    <small>Bounding box dan metrik performa</small>
                </div>
            </div>
        </div>
        """
    )

    with st.container(border=True):
        html(
            """
            <div class="parameter-panel-marker">
                <div>
                    <span>Parameter Inferensi</span>
                    <p>Atur tingkat keyakinan minimum dan resolusi input model.</p>
                </div>
            </div>
            """
        )

        confidence_col, image_size_col = st.columns(2, gap="large")

        with confidence_col:
            confidence = st.slider(
                "Confidence threshold",
                min_value=0.05,
                max_value=0.95,
                value=0.35,
                step=0.05,
                help="Prediksi di bawah nilai ini tidak akan ditampilkan.",
            )

        with image_size_col:
            image_size_options = [320, 416, 512, 640]
            imgsz = st.selectbox(
                "Ukuran inferensi",
                options=image_size_options,
                index=image_size_options.index(DEFAULT_IMAGE_SIZE),
                help=(
                    "Ukuran 320 memberikan performa paling ringan pada CPU. "
                    "Gunakan 416 untuk keseimbangan detail dan kecepatan, atau 640 untuk detail lebih tinggi."
                ),
            )

    return confidence, imgsz


# ============================================================
# Landing Page
# ============================================================

def render_landing(model_path: Optional[Path]):
    model_name = model_path.name if model_path is not None else "YOLOv11_best.pt"
    display_model_name = model_name.replace("YOLOv11", "YOLO11")

    html(
        f"""
        <div class="hero-wrap">
            <div class="eyebrow">Realtime Object Detection · YOLO11</div>
            <div class="hero-title">
                Pantau Kepatuhan<br><span>APD</span> Secara Realtime
            </div>
            <div class="hero-sub">
                Aplikasi web untuk mendeteksi penggunaan Alat Pelindung Diri melalui webcam.
                Sistem menampilkan hasil deteksi dalam bentuk bounding box, label kelas,
                confidence score, FPS, inference time, dan latency.
            </div>
            <div class="spec-row">
                <div class="spec-item">
                    <div class="spec-label">Input</div>
                    <div class="spec-value">Webcam</div>
                </div>
                <div class="spec-item">
                    <div class="spec-label">Model</div>
                    <div class="spec-value">YOLO11 · {display_model_name}</div>
                </div>
                <div class="spec-item">
                    <div class="spec-label">Output</div>
                    <div class="spec-value">Bounding Box</div>
                </div>
                <div class="spec-item">
                    <div class="spec-label">Metrik</div>
                    <div class="spec-value">FPS & Latency</div>
                </div>
            </div>
        </div>
        """
    )

    html('<div class="hazard-rule"></div>')

    html(
        """
        <div class="section-head">Ringkasan Sistem</div>
        <div class="section-desc">
            Sistem ini dirancang sebagai implementasi model deteksi APD berbasis YOLO11 pada aplikasi web.
        </div>
        """
    )

    left, right = st.columns([1.05, 1.35], gap="large")

    with left:
        html(
            """
            <div class="system-card">
                <div class="card-label">Tentang Sistem</div>
                <h3>Deteksi APD Berbasis Webcam</h3>
                <p>
                    Aplikasi ini memproses frame dari webcam secara realtime untuk mendeteksi
                    objek pekerja, helm keselamatan, dan rompi keselamatan. Hasil deteksi
                    ditampilkan dengan bounding box, label kelas, dan confidence score.
                </p>
                <div class="mini-metric-grid">
                    <div class="mini-metric">
                        <span>Input</span>
                        <b>Webcam</b>
                    </div>
                    <div class="mini-metric">
                        <span>Model</span>
                        <b>YOLO11</b>
                    </div>
                </div>
            </div>
            """
        )

    with right:
        html(
            f"""
            <div class="process-card">
                <div class="process-item">
                    <div class="process-icon">{icons.icon_camera(18, PRIMARY_COLOR)}</div>
                    <div>
                        <h4>Input Kamera</h4>
                        <p>Webcam menangkap kondisi secara langsung sebagai sumber data realtime.</p>
                    </div>
                </div>
                <div class="process-item">
                    <div class="process-icon">{icons.icon_gauge(18, PRIMARY_COLOR)}</div>
                    <div>
                        <h4>Inferensi Model</h4>
                        <p>Model YOLO11 membaca frame dan menghasilkan prediksi objek APD.</p>
                    </div>
                </div>
                <div class="process-item">
                    <div class="process-icon">{icons.icon_chart(18, PRIMARY_COLOR)}</div>
                    <div>
                        <h4>Output Evaluasi</h4>
                        <p>Sistem menampilkan bounding box, jumlah objek, FPS, inference time, dan latency.</p>
                    </div>
                </div>
            </div>
            """
        )

    html(
        """
        <div style="height:1.3rem;"></div>
        <div class="section-head">Fitur Utama</div>
        <div class="section-desc">
            Tampilan dibuat ringkas, fokus, dan mudah digunakan saat demo atau pengujian sistem.
        </div>
        """
    )

    f1, f2, f3 = st.columns(3, gap="medium")

    features = [
        (
            icons.icon_camera(20, PRIMARY_COLOR),
            "Webcam Realtime",
            "Kamera memproses frame secara langsung untuk menampilkan hasil deteksi.",
        ),
        (
            icons.icon_gauge(20, PRIMARY_COLOR),
            "FPS & Latency",
            "Sistem menampilkan kecepatan pemrosesan dan waktu inferensi.",
        ),
        (
            icons.icon_chart(20, PRIMARY_COLOR),
            "Ringkasan Deteksi",
            "Jumlah objek terdeteksi ditampilkan berdasarkan setiap kelas.",
        ),
    ]

    for col, (icon_svg, title, desc) in zip([f1, f2, f3], features):
        with col:
            html(
                f"""
                <div class="feat-card">
                    <div class="icon-box" style="margin-bottom:0.9rem;">{icon_svg}</div>
                    <div class="feat-title">{title}</div>
                    <div class="feat-desc">{desc}</div>
                </div>
                """
            )

    html(
        """
        <div style="height:1.3rem;"></div>
        <div class="section-head">Kelas yang Dikenali</div>
        <div class="section-desc">
            Kelas objek berikut disesuaikan dengan label dataset dan model hasil training.
        </div>
        """
    )

    class_cols = st.columns(len(CLASS_CARDS), gap="medium")

    for col, (name, _, icon_fn) in zip(class_cols, CLASS_CARDS):
        with col:
            html(
                f"""
                <div class="feat-card" style="padding:1.2rem;">
                    <div class="icon-box" style="margin-bottom:0.8rem;">
                        {icon_fn(18, PRIMARY_COLOR)}
                    </div>
                    <div class="feat-title" style="font-size:1rem;">
                        {name}
                    </div>
                    <div class="tally-row">
                        <div class="tally-name">
                            <span class="tally-swatch" style="background:var(--success);"></span>
                            Terdeteksi
                        </div>
                    </div>
                    <div class="tally-row">
                        <div class="tally-name">
                            <span class="tally-swatch" style="background:var(--primary);"></span>
                            Dipantau
                        </div>
                    </div>
                </div>
                """
            )


# ============================================================
# Realtime Webcam Processor
# ============================================================

class RealtimeYOLOProcessor(VideoProcessorBase):
    def __init__(self, model_path: str, confidence: float, image_size: int):
        self.model = load_model(model_path)
        self.confidence = confidence
        self.image_size = image_size
        self.lock = threading.Lock()
        self.prev_time = time.perf_counter()

        self.metrics = {
            "fps": 0.0,
            "inference_ms": 0.0,
            "latency_ms": 0.0,
            "objects": 0,
            "summary": "Belum ada objek terdeteksi.",
            "counts": {},
        }

    def recv(self, frame):
        img_bgr = frame.to_ndarray(format="bgr24")

        start_time = time.perf_counter()

        results = self.model.predict(
            source=img_bgr,
            conf=self.confidence,
            imgsz=self.image_size,
            max_det=MAX_DETECTIONS,
            verbose=False,
        )

        latency_ms = (time.perf_counter() - start_time) * 1000

        result = results[0]
        annotated_bgr = result.plot()

        now = time.perf_counter()
        elapsed = max(now - self.prev_time, 1e-6)
        self.prev_time = now
        fps = 1.0 / elapsed

        boxes = result.boxes
        objects = len(boxes) if boxes is not None else 0

        counter = {}

        if boxes is not None and len(boxes) > 0:
            cls_ids = boxes.cls.detach().cpu().numpy().astype(int)

            for cls_id in cls_ids:
                class_name = get_class_name(self.model.names, int(cls_id))
                counter[class_name] = counter.get(class_name, 0) + 1

        speed = getattr(result, "speed", {}) or {}
        inference_ms = float(speed.get("inference", 0.0))

        with self.lock:
            self.metrics = {
                "fps": fps,
                "inference_ms": inference_ms,
                "latency_ms": latency_ms,
                "objects": objects,
                "summary": summarize_counter(counter),
                "counts": counter,
            }

        return av.VideoFrame.from_ndarray(annotated_bgr, format="bgr24")

    def get_metrics(self):
        with self.lock:
            return dict(self.metrics)


# ============================================================
# Detection Page
# ============================================================

def render_detection(model_path: Optional[Path]):
    html(
        """
        <div class="detect-hero">
            <div>
                <div class="eyebrow">Live Monitor</div>
                <div class="section-head" style="margin-bottom:0.25rem;">
                    Deteksi Webcam Realtime
                </div>
                <div class="section-desc" style="margin-bottom:0;">
                    Aktifkan kamera untuk menjalankan deteksi APD
                    secara langsung melalui webcam.
                </div>
            </div>
            <div class="live-chip">
                <span></span>
                Camera Ready
            </div>
        </div>
        """
    )

    confidence, imgsz = render_detection_configuration(model_path)

    if model_path is None:
        html(
            """
            <div class="detect-status warning">
                <div class="detect-status-icon">!</div>
                <div>
                    <h4>Model YOLO11 belum ditemukan</h4>
                    Letakkan file <b>YOLO11s_APD_best.pt</b>
                    ke folder <b>models</b>, lalu jalankan ulang aplikasi.
                </div>
            </div>
            """
        )
        return

    # Memuat model sebelum webcam dijalankan.
    try:
        load_model(str(model_path))
    except Exception as error:
        st.error(
            "Model YOLO11 gagal dimuat. "
            "Periksa file model dan dependensi Ultralytics/OpenCV."
        )
        st.exception(error)
        return

    html(
        """
        <div class="camera-panel">
            <div class="camera-topbar">
                <span>Camera Feed</span>
                <b>Standby Mode</b>
            </div>
        </div>
        """
    )

    rtc_configuration = RTCConfiguration(
        {
            "iceServers": [
                {
                    "urls": [
                        "stun:stun.l.google.com:19302"
                    ]
                }
            ]
        }
    )

    ctx = webrtc_streamer(
        key="apd-realtime-yolo",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=rtc_configuration,
        video_processor_factory=lambda: RealtimeYOLOProcessor(
            str(model_path),
            confidence,
            imgsz,
        ),
        media_stream_constraints={
            "video": {
                "width": {"ideal": CAMERA_WIDTH},
                "height": {"ideal": CAMERA_HEIGHT},
                "frameRate": {
                    "ideal": CAMERA_FPS,
                    "max": CAMERA_FPS,
                },
            },
            "audio": False,
        },
        async_processing=True,
    )

    inject_webrtc_control_style()

    if not ctx.state.playing:
        html(
            f"""
            <div class="camera-helper">
                <div class="camera-helper-icon">{icons.icon_camera(20, PRIMARY_COLOR)}</div>
                <div>
                    <h4>Kamera belum aktif</h4>
                    <p>
                        Klik tombol <b>START</b> pada panel webcam, lalu pilih perangkat kamera jika diminta.
                        Setelah izin kamera diberikan, sistem akan mulai menampilkan hasil deteksi secara realtime.
                    </p>
                </div>
            </div>
            """
        )

    html(
        """
        <div class="section-head detect-metric-title">
            Performa Sistem
        </div>
        <div class="section-desc">
            Metrik diperbarui selama webcam berjalan.
        </div>
        """
    )

    readout_slot = st.empty()
    tally_slot = st.empty()

    if not ctx.state.playing:
        slot_html(
            readout_slot,
            """
            <div class="readout-grid">
                <div class="readout">
                    <div class="readout-label">FPS</div>
                    <div class="readout-value">-</div>
                </div>
                <div class="readout">
                    <div class="readout-label">Inference</div>
                    <div class="readout-value">-</div>
                </div>
                <div class="readout">
                    <div class="readout-label">Latency</div>
                    <div class="readout-value">-</div>
                </div>
                <div class="readout">
                    <div class="readout-label">Objek</div>
                    <div class="readout-value">-</div>
                </div>
            </div>
            """
        )

        slot_html(
            tally_slot,
            """
            <div class="feat-card" style="margin-top:1.2rem;">
                <div class="feat-title" style="font-size:1.05rem;margin-bottom:0.6rem;">
                    Ringkasan Deteksi
                </div>
                <div class="feat-desc">
                    Aktifkan kamera untuk mulai membaca jumlah objek yang terdeteksi.
                </div>
            </div>
            """
        )

    while ctx.state.playing:
        if ctx.video_processor:
            metrics = ctx.video_processor.get_metrics()

            fps_class = (
                "safe"
                if metrics["fps"] >= 15
                else ("warn" if metrics["fps"] >= 8 else "bad")
            )

            slot_html(
                readout_slot,
                f"""
                <div class="readout-grid">
                    <div class="readout">
                        <div class="readout-label">FPS</div>
                        <div class="readout-value {fps_class}">{metrics["fps"]:.1f}</div>
                    </div>
                    <div class="readout">
                        <div class="readout-label">Inference</div>
                        <div class="readout-value">{metrics["inference_ms"]:.1f}
                            <span style="font-size:0.9rem;color:var(--muted);">ms</span>
                        </div>
                    </div>
                    <div class="readout">
                        <div class="readout-label">Latency</div>
                        <div class="readout-value">{metrics["latency_ms"]:.1f}
                            <span style="font-size:0.9rem;color:var(--muted);">ms</span>
                        </div>
                    </div>
                    <div class="readout">
                        <div class="readout-label">Objek</div>
                        <div class="readout-value">{metrics["objects"]}</div>
                    </div>
                </div>
                """
            )

            counts = metrics.get("counts", {})

            if counts:
                rows = ""

                for label, count in sorted(counts.items(), key=lambda x: -x[1]):
                    color = color_for_label(label)

                    rows += clean_html(
                        f"""
                        <div class="tally-row">
                            <div class="tally-name">
                                <span class="tally-swatch" style="background:{color};"></span>
                                {label}
                            </div>
                            <div class="tally-count">{count}</div>
                        </div>
                        """
                    )

                slot_html(
                    tally_slot,
                    f"""
                    <div class="feat-card" style="margin-top:1.2rem;">
                        <div class="feat-title" style="font-size:1.05rem;margin-bottom:0.6rem;">
                            Ringkasan Deteksi
                        </div>
                        {rows}
                    </div>
                    """
                )
            else:
                slot_html(
                    tally_slot,
                    """
                    <div class="feat-card" style="margin-top:1.2rem;">
                        <div class="feat-title" style="font-size:1.05rem;margin-bottom:0.6rem;">
                            Ringkasan Deteksi
                        </div>
                        <div class="feat-desc">Belum ada objek terdeteksi.</div>
                    </div>
                    """
                )

        time.sleep(0.5)


# ============================================================
# Main
# ============================================================

def main():
    model_path = find_model()
    render_top_navigation()

    if st.session_state.page == "landing":
        render_landing(model_path)
    else:
        render_detection(model_path)


if __name__ == "__main__":
    main()
