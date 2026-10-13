import os
import ctypes
import win32com.client

def create_shortcuts():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(project_dir, 'assets', 'icon.ico')

    # Antigravity IDE executable & profile
    antigravity_exe = r'C:\Users\netse\AppData\Local\Programs\Antigravity IDE\Antigravity IDE.exe'
    profile_dir = r'C:\Google antigravity paulnteddy'
    workspace_dir = project_dir

    # Arguments: Open workspace with the active user profile
    args = f'--user-data-dir="{profile_dir}" "{workspace_dir}"'

    # Desktop locations
    desktop_candidates = [
        r'C:\Users\netse\OneDrive\바탕 화면',
        os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'OneDrive', '바탕 화면')
    ]
    desktop_dirs = []
    for d in desktop_candidates:
        if d and os.path.exists(d) and d not in desktop_dirs:
            desktop_dirs.append(d)

    print(f"Target Executable: {antigravity_exe} (exists: {os.path.exists(antigravity_exe)})")
    print(f"Arguments: {args}")
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
            shortcut.TargetPath = antigravity_exe
            shortcut.Arguments = args
            shortcut.WorkingDirectory = workspace_dir
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
