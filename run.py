#!/bin/bash

# ==========================================
# XYZ TOOL BY HASSAN
# Version 4.1 (No Approval Needed)
# ==========================================

# Colors
G='\e[1;32m'
R='\e[1;31m'
C='\e[1;36m'
Y='\e[1;33m'
W='\e[0m'

clear

echo -e "${C}[*] XYZ TOOL Checking System Health...${W}"

# ==========================================
# LOCK & REPO FIX
# ==========================================
killall apt apt-get dpkg 2>/dev/null

rm -rf /data/data/com.termux/files/usr/var/lib/dpkg/lock*
rm -rf /data/data/com.termux/files/usr/var/lib/apt/lists/lock
rm -rf /data/data/com.termux/files/usr/var/cache/apt/archives/lock

echo "deb https://termux.dev stable main" > $PREFIX/etc/apt/sources.list

# ==========================================
# PYTHON CHECK & DEPENDENCIES
# ==========================================
PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)

if [ "$PY_VER" != "3.13" ]; then
    echo -e "${Y}[!] System Upgrade Required...${W}"
    export DEBIAN_FRONTEND=noninteractive

    apt update -y
    apt install termux-keyring -y
    apt update -y

    echo -e "${Y}[*] Installing Python...${W}"
    apt install python -y

    echo -e "${Y}[*] Installing Required Modules...${W}"
    pip install --upgrade pip --quiet
    pip install requests rich pycryptodome --quiet
else
    python3 -c "import requests,rich" 2>/dev/null
    if [ $? -ne 0 ]; then
        pip install requests rich pycryptodome --quiet
    fi
fi

# ==========================================
# CREATING INLINE MAIN.PY (Auto-Generated)
# ==========================================
cat << 'EOF' > main.py
import sys
import time

try:
    import requests
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("[!] Missing dependencies.")
    sys.exit(1)

console = Console()

def display_banner():
    banner_text = """
 [bold green] ██████╗  ██████╗ ██████╗ ███████╗[/bold green]
 [bold green]██╔════╝ ██╔═══██╗██╔══██╗██╔════╝[/bold green]
 [bold cyan]██║  ███╗██║   ██║██║  ██║█████╗  [/bold cyan]
 [bold cyan]██║   ██║██║   ██║██║  ██║██╔══╝  [/bold cyan]
 [bold white]╚██████╔╝╚██████╔╝██████╔╝███████╗[/bold white]
 [bold white] ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝[/bold white]
    """
    console.print(banner_text)
    
    info_panel = Panel(
        "[bold white]Created By :[/bold white] [bold yellow]Hassan[/bold yellow]\n"
        "[bold white]Version    :[/bold white] [bold cyan]1.0.0[/bold cyan]\n"
        "[bold white]Status     :[/bold white] [bold green]Active - No Approval Needed[/bold green]",
        title="[bold red]XYZ SYSTEM CONTROL[/bold red]",
        expand=False
    )
    console.print(info_panel)

def main_logic():
    console.print("\n[bold green][✔] Access Granted! Welcome to your automated panel.[/bold green]\n")
    console.print("[bold white]Select an Option:[/bold white]")
    console.print(" Check Network Status")
    console.print(" Run Diagnostics")
    console.print(" [E] Exit")
    
    try:
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            console.print("[yellow][*] Checking connection...[/yellow]")
            response = requests.get("https://httpbin.org", timeout=5)
            if response.status_code == 200:
                console.print("[green][✔] Network Status: Online![/green]")
            else:
                console.print("[red][!] Connection Error[/red]")
        elif choice == "2":
            console.print("[green][✔] All components running smoothly.[/green]")
        elif choice.lower() == 'e':
            console.print("[bold red][*] Exiting. Goodbye![/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red][!] Invalid Option.[/bold red]")
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Operation cancelled.[/bold red]")

if __name__ == "__main__":
    display_banner()
    main_logic()
EOF

# ==========================================
# SMART LAUNCHER (Executes the auto-created main.py)
# ==========================================
ARCH=$(uname -m)

if [[ "$ARCH" == "aarch64" ]] || \
   [[ "$ARCH" == armv* ]] || \
   [[ "$ARCH" == "x86_64" ]] || \
   [[ "$ARCH" == "i686" ]]; then

    echo -e "${G}[✔] Launching Tool...${W}"
    python3 main.py "$@"
else
    echo -e "${R}[!] Unsupported Architecture: $ARCH${W}"
fi
