import re

with open('c:/Users/tmiya/Documents/HTML/kajiya/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = "body { margin: 0; font-family: sans-serif; background-color: #F4EFE6; }"
css_new = """body { margin: 0; font-family: sans-serif; background-color: #1a1a1a; }
    .bg-glass { background-color: rgba(20, 15, 10, 0.85); backdrop-filter: blur(8px); border: 1px solid rgba(212, 175, 55, 0.3); color: #F4EFE6; }
    .bg-glass-light { background-color: rgba(255, 255, 255, 0.1); backdrop-filter: blur(4px); border: 1px solid rgba(255, 255, 255, 0.2); }
    .bg-glass-panel { background-color: rgba(30, 25, 20, 0.7); backdrop-filter: blur(4px); border: 1px solid rgba(212, 175, 55, 0.2); color: #E0D0B0; }
    .bg-image { background-size: cover; background-position: center; background-attachment: fixed; transition: background-image 0.5s ease-in-out; }
    /* Enhance specific text colors inside glass panels */
    .text-dark { color: #2C3E50 !important; }
"""
content = content.replace(css_old, css_new)

# 2. Main App structure
app_ret_old = """      if (!isLoaded) return null;

      return (
        <div className="flex flex-col h-[100dvh] bg-[#F4EFE6] overflow-hidden">"""
app_ret_new = """      if (!isLoaded) return null;

      const getBgImage = () => {
        if (gameState === 'opening') return 'url("./assets/images/bg_opening.png")';
        if (gameState === 'craft') return 'url("./assets/images/bg_forge.png")';
        if (gameState === 'shop' || gameState === 'dealer') return 'url("./assets/images/bg_shop.png")';
        return 'url("./assets/images/bg_town.png")';
      };

      return (
        <div className="flex flex-col h-[100dvh] bg-image overflow-hidden" style={{ backgroundImage: getBgImage() }}>"""
content = content.replace(app_ret_old, app_ret_new)

# 3. Opening View
open_old = '<div className="fixed inset-0 bg-black text-white flex flex-col items-center justify-center z-50 p-6 overflow-y-auto fade-in">'
open_new = '<div className="fixed inset-0 bg-black/60 backdrop-blur-sm text-white flex flex-col items-center justify-center z-50 p-6 overflow-y-auto fade-in">'
content = content.replace(open_old, open_new)

open_box_old = '<div className="text-base md:text-lg leading-loose text-gray-300 space-y-4 mb-12 bg-white/5 p-8 rounded border border-[#3E2723] shadow-inner text-left">'
open_box_new = '<div className="text-base md:text-lg leading-loose text-gray-300 space-y-4 mb-12 bg-black/60 backdrop-blur-md p-8 rounded border border-[#D4AF37]/50 shadow-[0_0_15px_rgba(0,0,0,0.8)] text-left">'
content = content.replace(open_box_old, open_box_new)

# 4. Header & Sidebar
header_old = '<div className="flex-shrink-0 flex justify-between items-center p-3 bg-[#3E2723] text-[#F4EFE6] border-b-4 border-[#D4AF37] relative z-20">'
header_new = '<div className="flex-shrink-0 flex justify-between items-center p-3 bg-glass border-b-4 border-[#D4AF37] relative z-20">'
content = content.replace(header_old, header_new)

sidebar_old = '<div className="w-16 md:w-64 flex-shrink-0 bg-[#3E2723] text-[#F4EFE6] p-2 md:p-4 flex flex-col border-r-2 border-[#D4AF37] overflow-y-auto z-10">'
sidebar_new = '<div className="w-16 md:w-64 flex-shrink-0 bg-glass p-2 md:p-4 flex flex-col border-r-2 border-[#D4AF37] overflow-y-auto z-10">'
content = content.replace(sidebar_old, sidebar_new)

# 5. Text colors & Panels
content = content.replace('bg-white', 'bg-glass-panel')
content = content.replace('bg-gray-50', 'bg-black/40')
content = content.replace('bg-gray-100', 'bg-black/50')
content = content.replace('bg-gray-200', 'bg-black/60')

content = content.replace('text-gray-500', 'text-gray-400')
content = content.replace('text-gray-600', 'text-gray-300')
content = content.replace('text-gray-700', 'text-gray-200')
content = content.replace('text-gray-800', 'text-gray-100')

content = content.replace('text-[#2C3E50]', 'text-[#F4EFE6]')
content = content.replace('text-[#3E2723]', 'text-[#E0D0B0]')

# Fix specific buttons that should remain visible
content = content.replace('bg-[#3E2723] text-[#D4AF37]', 'bg-[#D4AF37] text-dark font-bold')

# Main Menu Container
content = content.replace('<div className="bg-glass-panel rounded shadow-md border border-[#D4AF37]/20', '<div className="bg-glass rounded shadow-lg border border-[#D4AF37]/50')
content = content.replace('<div className="p-4 bg-black/40 border-b', '<div className="p-4 bg-black/60 border-b border-[#D4AF37]/30')

with open('c:/Users/tmiya/Documents/HTML/kajiya/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete.")
