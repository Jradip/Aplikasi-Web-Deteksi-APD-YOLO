"""
Kumpulan icon SVG outline minimalis (stroke-based, satu warna).
Sengaja tidak pakai emoji atau icon font pihak ketiga supaya konsisten
dengan tema visual aplikasi dan ringan (tanpa request jaringan tambahan).

Semua icon menerima parameter `color` dan `size` agar bisa dipakai ulang
di konteks berbeda (sidebar brand, hero badge, kartu fitur, dsb).
"""

_STROKE = (
    'fill="none" stroke="{color}" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"'
)


def _svg(inner: str, size: int, color: str) -> str:
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'xmlns="http://www.w3.org/2000/svg">{inner.format(color=color)}</svg>'
    )


def icon_helmet(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M4 14.5C4 9.3 7.8 5 12 5s8 4.3 8 9.5" />'
        f'<path {_STROKE} d="M3.5 14.5h17" />'
        f'<path {_STROKE} d="M5.5 14.5v2.2c0 1 .8 1.8 1.8 1.8h9.4c1 0 1.8-.8 1.8-1.8v-2.2" />'
        f'<path {_STROKE} d="M12 5V3" />'
    )
    return _svg(inner, size, color)


def icon_vest(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M8 4l4 2 4-2 3 3-2 2v11a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V9L3 7l3-3z" />'
        f'<path {_STROKE} d="M9.5 6.5v14" />'
        f'<path {_STROKE} d="M14.5 6.5v14" />'
    )
    return _svg(inner, size, color)


def icon_gloves(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M7 11V5.5a1.5 1.5 0 0 1 3 0V10" />'
        f'<path {_STROKE} d="M10 10V4.5a1.5 1.5 0 0 1 3 0V10" />'
        f'<path {_STROKE} d="M13 10V5.5a1.5 1.5 0 0 1 3 0V12" />'
        f'<path {_STROKE} d="M16 12V8a1.5 1.5 0 0 1 3 0v7c0 3.3-2.2 6-6 6H9.5C7 21 5 18.8 5 16.2v-3.7c0-.9.7-1.5 1.5-1.5S8 11.6 8 12.5" />'
    )
    return _svg(inner, size, color)


def icon_mask(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M4 11c0-1.5 1-2.5 2.5-2.8 3.6-.7 7.4-.7 11 0C19 8.5 20 9.5 20 11v1.3c0 3.6-3.6 6.2-8 6.2s-8-2.6-8-6.2V11z" />'
        f'<path {_STROKE} d="M4 12.5c-1 .2-2 .9-2 2" />'
        f'<path {_STROKE} d="M20 12.5c1 .2 2 .9 2 2" />'
        f'<path {_STROKE} d="M9 12.5c.7.6 1.6 1 3 1s2.3-.4 3-1" />'
    )
    return _svg(inner, size, color)


def icon_boots(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M9 3v8.5l-5 3.2c-.6.4-1 1-1 1.8V18a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5c0-3-1.6-5.6-4-7V3" />'
        f'<path {_STROKE} d="M9 3h5" />'
        f'<path {_STROKE} d="M3 19h17" />'
    )
    return _svg(inner, size, color)


def icon_camera(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M4 8.5A1.5 1.5 0 0 1 5.5 7h2l1-2h7l1 2h2A1.5 1.5 0 0 1 20 8.5v9A1.5 1.5 0 0 1 18.5 19h-13A1.5 1.5 0 0 1 4 17.5v-9z" />'
        f'<circle {_STROKE} cx="12" cy="13" r="3.4" />'
    )
    return _svg(inner, size, color)


def icon_gauge(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M4 14a8 8 0 1 1 16 0" />'
        f'<path {_STROKE} d="M12 14l4-5" />'
        f'<path {_STROKE} d="M12 14v0" />'
    )
    return _svg(inner, size, color)


def icon_chart(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M4 20V4" />'
        f'<path {_STROKE} d="M4 20h16" />'
        f'<rect {_STROKE} x="7" y="13" width="2.6" height="7" />'
        f'<rect {_STROKE} x="12" y="9" width="2.6" height="11" />'
        f'<rect {_STROKE} x="17" y="5" width="2.6" height="15" />'
    )
    return _svg(inner, size, color)


def icon_shield(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M12 3l7 3v5.5c0 4.6-3 7.9-7 9.5-4-1.6-7-4.9-7-9.5V6z" />'
        f'<path {_STROKE} d="M9 12.2l2 2 4-4.4" />'
    )
    return _svg(inner, size, color)


def icon_info(size=22, color="currentColor"):
    inner = (
        f'<circle {_STROKE} cx="12" cy="12" r="8.5" />'
        f'<path {_STROKE} d="M12 11v5.5" />'
        f'<path {_STROKE} d="M12 7.8v.1" />'
    )
    return _svg(inner, size, color)


def icon_alert(size=22, color="currentColor"):
    inner = (
        f'<path {_STROKE} d="M12 4 21 19H3z" />'
        f'<path {_STROKE} d="M12 10v4" />'
        f'<path {_STROKE} d="M12 16.5v.1" />'
    )
    return _svg(inner, size, color)


def icon_check(size=22, color="currentColor"):
    inner = (
        f'<circle {_STROKE} cx="12" cy="12" r="8.5" />'
        f'<path {_STROKE} d="M8.2 12.3l2.6 2.6 5-5.4" />'
    )
    return _svg(inner, size, color)
