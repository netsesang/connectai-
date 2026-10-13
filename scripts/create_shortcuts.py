import os
import ctypes
import win32com.client

def create_shortcuts():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(project_dir, 'assets', 'icon.ico')
    vbs_path = os.path.join(project_dir, 'launch_app.vbs')
    wscript_path = r'C:\Windows\System32\wscript.exe'

    desktop_candidates = [
        r'C:\Users\netse\OneDrive\바탕 화면',
        os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'OneDrive', '바탕 화면')
    ]
    desktop_dirs = []
    for d in desktop_candidates:
        if d and os.path.exists(d) and d not in desktop_dirs:
            desktop_dirs.append(d)

    print(f"Target Launcher: {vbs_path} (exists: {os.path.exists(vbs_path)})")
    print(f"Icon: {icon_path} (exists: {os.path.exists(icon_path)})")

    shell = win32com.client.Dispatch('WScript.Shell')

    for desktop in desktop_dirs:
        shortcut_names = [
            '97.Connect AI Lab (AI 1인 기업 · 에이전트 팀).lnk',
            'Connect AI.lnk'
        ]

        for name in shortcut_names:
            lnk_path = os.path.join(desktop, name)
            shortcut = shell.CreateShortcut(lnk_path)
            shortcut.TargetPath = wscript_path
            shortcut.Arguments = f'"{vbs_path}"'
            shortcut.WorkingDirectory = project_dir
            shortcut.IconLocation = f"{icon_path},0"
            shortcut.Description = "Connect AI — AI 1인 기업 · 나만의 에이전트 팀 · 제2의 두뇌"
            shortcut.Save()
            print(f"Updated shortcut: {lnk_path}")

    # Refresh Windows Shell Icon Cache
    try:
        SHCNE_ASSOCCHANGED = 0x08000000
        SHCNF_IDLIST = 0x0000
        ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, None, None)
        print("Windows Shell icon cache refreshed successfully.")
    except Exception as e:
        print(f"Warning: Failed to refresh shell cache: {e}")

if __name__ == '__main__':
    create_shortcuts()
