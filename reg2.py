#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import os
import string
import subprocess
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ==============================================================================
# CẤU HÌNH GIAO DIỆN HACKER & MÀU SẮC
# ==============================================================================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ==============================================================================
# DỮ LIỆU TẠO TÀI KHOẢN (DATA)
# ==============================================================================
VIETNAMESE_FIRST_NAMES = [
    'Anh', 'Bảo', 'Châu', 'Dũng', 'Đức', 'Giang', 'Hà', 'Hải', 'Hiếu', 'Hoàng',
    'Hùng', 'Huy', 'Khánh', 'Khoa', 'Kiên', 'Linh', 'Long', 'Mai', 'Minh', 'Nam',
    'Ngọc', 'Nhung', 'Phong', 'Phương', 'Quang', 'Quyên', 'Sơn', 'Tâm', 'Thảo', 'Thư',
    'Trâm', 'Trinh', 'Trung', 'Tuấn', 'Tú', 'Uyên', 'Vân', 'Việt', 'Xuân', 'Yến'
]

VIETNAMESE_LAST_NAMES = [
    'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh', 'Phan', 'Vũ', 'Võ', 'Đặng',
    'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý'
]

# ==============================================================================
# CÁC HÀM HỖ TRỢ (UTILITIES)
# ==============================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = f"""
{Colors.GREEN}
████████╗██████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗██║ ██╔╝
   ██║   ██║  ██║█████╔╝ 
   ██║   ██║  ██║██╔═██╗ 
   ██║   ██████╔╝██║  ██╗
   ╚═╝   ╚═════╝ ╚═╝  ╚═╝
{Colors.ENDC}
{Colors.CYAN}╔══════════════════════════════════════════════════╗
║  {Colors.BOLD}ADMIN       : DUONG PHUNG{Colors.ENDC}{Colors.CYAN}                       ║
║  {Colors.BOLD}ZALO GROUP  : (Nhập link nhóm của bạn){Colors.ENDC}{Colors.CYAN}          ║
║  {Colors.BOLD}TOOL        : AUTO REG BUMX VIP{Colors.ENDC}{Colors.CYAN}                 ║
║  {Colors.BOLD}VERSION     : 2.0 (Premium){Colors.ENDC}{Colors.CYAN}                     ║
╚══════════════════════════════════════════════════╝{Colors.ENDC}
    """
    print(banner)

def remove_vietnamese_accents(text):
    """Chuyển đổi tiếng Việt có dấu sang không dấu"""
    accent_map = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
        'đ': 'd',
    }
    result = ''
    for char in text.lower():
        result += accent_map.get(char, char)
    return result

def generate_vietnamese_email():
    """Tạo email ảo dựa trên tên người Việt"""
    last_name = random.choice(VIETNAMESE_LAST_NAMES)
    first_name = random.choice(VIETNAMESE_FIRST_NAMES)
    
    last_name_no_accent = remove_vietnamese_accents(last_name)
    first_name_no_accent = remove_vietnamese_accents(first_name)
    
    random_number = random.randint(10000, 99999)
    email = f"{last_name_no_accent}{first_name_no_accent}{random_number}@gmail.com"
    return email

def generate_secure_password():
    """Tạo mật khẩu ngẫu nhiên 8-14 ký tự (Hoa + Thường + Số)"""
    length = random.randint(8, 14)
    # Đảm bảo có ít nhất 1 chữ hoa, 1 chữ thường, 1 số
    chars_upper = string.ascii_uppercase
    chars_lower = string.ascii_lowercase
    chars_digits = string.digits
    
    # Chọn trước mỗi loại 1 ký tự
    password_list = [
        random.choice(chars_upper),
        random.choice(chars_lower),
        random.choice(chars_digits)
    ]
    
    # Điền nốt các ký tự còn lại
    all_chars = chars_upper + chars_lower + chars_digits
    for _ in range(length - 3):
        password_list.append(random.choice(all_chars))
        
    random.shuffle(password_list)
    return "".join(password_list)

def setup_chrome_driver():
    """Cấu hình và khởi chạy Chrome Driver"""
    chrome_options = Options()
    # Chạy ẩn (Headless) - Bỏ comment dòng dưới nếu muốn xem trình duyệt chạy
    chrome_options.add_argument('--headless=new') 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3') # Tắt log rác
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    service = Service()
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"{Colors.FAIL}[!] Lỗi khởi tạo Chrome: {e}{Colors.ENDC}")
        return None

# ==============================================================================
# HÀM ĐĂNG KÝ CHÍNH (CORE LOGIC)
# ==============================================================================
def register_account(email, password, referral_code):
    driver = None
    try:
        print(f"{Colors.CYAN}[*] Đang khởi tạo session...{Colors.ENDC}")
        driver = setup_chrome_driver()
        if not driver: return False
        
        url = "https://app.bumx.vn/register"
        print(f"{Colors.CYAN}[*] Đang truy cập: {url}{Colors.ENDC}")
        driver.get(url)
        
        wait = WebDriverWait(driver, 15)
        
        # --- BƯỚC 1: NHẬP EMAIL ---
        print(f"{Colors.BLUE}[+] Đang nhập Email...{Colors.ENDC}")
        # Tìm input có placeholder chứa 'email'
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='email']")))
        email_input.clear()
        email_input.send_keys(email)
        time.sleep(0.5)
        
        # --- BƯỚC 2: NHẬP MẬT KHẨU ---
        print(f"{Colors.BLUE}[+] Đang thiết lập Mật khẩu bảo mật...{Colors.ENDC}")
        password_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
        
        if len(password_inputs) >= 2:
            # Nhập mật khẩu
            password_inputs[0].clear()
            password_inputs[0].send_keys(password)
            time.sleep(0.2)
            # Nhập lại mật khẩu
            password_inputs[1].clear()
            password_inputs[1].send_keys(password)
            time.sleep(0.2)
        else:
            print(f"{Colors.FAIL}[!] Lỗi: Không tìm thấy trường mật khẩu!{Colors.ENDC}")
            return False

        # --- BƯỚC 3: NHẬP MÃ GIỚI THIỆU (CHÍNH XÁC) ---
        if referral_code and referral_code.strip() != "":
            print(f"{Colors.WARNING}[#] Phát hiện mã giới thiệu: {Colors.BOLD}{referral_code}{Colors.ENDC}")
            try:
                # Tìm input có placeholder chính xác như trong ảnh "Nhập mã giới thiệu từ đại lý"
                # Sử dụng XPath contains để tìm chính xác hơn
                ref_input = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'mã giới thiệu') or contains(@placeholder, 'đại lý')]")
                
                # Cuộn tới phần tử để đảm bảo nó hiển thị
                driver.execute_script("arguments[0].scrollIntoView(true);", ref_input)
                time.sleep(0.5)
                
                ref_input.clear()
                ref_input.send_keys(referral_code.strip())
                print(f"{Colors.GREEN}[✓] Đã điền mã giới thiệu thành công!{Colors.ENDC}")
                time.sleep(0.5)
            except Exception as e:
                print(f"{Colors.FAIL}[!] Lỗi nhập mã giới thiệu: Không tìm thấy ô nhập liệu đúng cấu trúc.{Colors.ENDC}")
                # Fallback: Thử tìm input type=text cuối cùng nếu tìm theo placeholder thất bại
                try:
                    all_inputs = driver.find_elements(By.TAG_NAME, "input")
                    if len(all_inputs) > 3:
                        all_inputs[-1].send_keys(referral_code.strip()) # Thường là ô cuối cùng
                        print(f"{Colors.WARNING}[!] Đã thử điền vào ô input cuối cùng.{Colors.ENDC}")
                except:
                    pass

        # --- BƯỚC 4: SUBMIT FORM ---
        print(f"{Colors.CYAN}[*] Đang gửi yêu cầu đăng ký...{Colors.ENDC}")
        
        # Tìm nút đăng ký thông minh hơn
        submit_btn = None
        # Cách 1: Tìm theo text
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "ĐĂNG KÝ" in btn.text.upper() or "REGISTER" in btn.text.upper():
                submit_btn = btn
                break
        
        # Cách 2: Tìm theo type submit
        if not submit_btn:
            try: submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            except: pass
            
        if submit_btn:
            driver.execute_script("arguments[0].click();", submit_btn)
            
            # Đợi phản hồi từ server
            time.sleep(5)
            
            # Check kết quả
            curr_url = driver.current_url
            page_source = driver.page_source.lower()
            
            if "login" in curr_url or "dashboard" in curr_url or "thành công" in page_source or "success" in page_source:
                return True
            else:
                # Kiểm tra xem có lỗi hiển thị không
                return False
        else:
            print(f"{Colors.FAIL}[!] Không tìm thấy nút Đăng ký!{Colors.ENDC}")
            return False

    except Exception as e:
        print(f"{Colors.FAIL}[ERROR] Exception: {e}{Colors.ENDC}")
        return False
    finally:
        if driver:
            driver.quit()

def save_log(email, password, ref_code, status):
    """Lưu log ra file"""
    timestamp = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    status_text = "SUCCESS" if status else "FAILED"
    
    log_line = f"[{timestamp}] | EMAIL: {email} | PASS: {password} | REF: {ref_code} | STATUS: {status_text}\n"
    
    with open("tdk_accounts.txt", "a", encoding="utf-8") as f:
        f.write(log_line)

# ==============================================================================
# HÀM MAIN
# ==============================================================================
def main():
    print_banner()
    
    # --- NHẬP MÃ GIỚI THIỆU TỪ NGƯỜI DÙNG ---
    print(f"{Colors.WARNING}╔══════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.WARNING}║  NHẬP MÃ GIỚI THIỆU (Enter để bỏ qua)            ║{Colors.ENDC}")
    print(f"{Colors.WARNING}╚══════════════════════════════════════════════════╝{Colors.ENDC}")
    user_ref_code = input(f"{Colors.GREEN}➤ Mã giới thiệu: {Colors.ENDC}").strip()
    
    if user_ref_code:
        print(f"\n{Colors.CYAN}[INFO] Tool sẽ tự động điền mã: {Colors.BOLD}{user_ref_code}{Colors.ENDC}")
    else:
        print(f"\n{Colors.CYAN}[INFO] Chạy chế độ không có mã giới thiệu.{Colors.ENDC}")
    
    print(f"\n{Colors.GREEN}{'='*60}")
    print(f"      BẮT ĐẦU TIẾN TRÌNH AUTO REG ACC - TDK TOOLS")
    print(f"{'='*60}{Colors.ENDC}\n")
    
    total_runs = 2 # Số lượng tài khoản muốn tạo
    
    for i in range(total_runs):
        print(f"{Colors.HEADER}┌── [ ACCOUNT {i+1}/{total_runs} ] ────────────────────────────────┐{Colors.ENDC}")
        
        # Sinh data
        current_email = generate_vietnamese_email()
        current_pass = generate_secure_password()
        
        print(f"{Colors.HEADER}│{Colors.ENDC}  Email : {Colors.BOLD}{current_email}{Colors.ENDC}")
        print(f"{Colors.HEADER}│{Colors.ENDC}  Pass  : {Colors.BOLD}{current_pass}{Colors.ENDC}")
        
        # Thực thi
        is_success = register_account(current_email, current_pass, user_ref_code)
        
        # Lưu kết quả
        save_log(current_email, current_pass, user_ref_code, is_success)
        
        if is_success:
            print(f"{Colors.HEADER}│{Colors.ENDC}")
            print(f"{Colors.HEADER}│{Colors.ENDC}  {Colors.GREEN}✔ REG SUCCESSFUL!{Colors.ENDC}")
        else:
            print(f"{Colors.HEADER}│{Colors.ENDC}")
            print(f"{Colors.HEADER}│{Colors.ENDC}  {Colors.FAIL}✖ REG FAILED!{Colors.ENDC}")
            
        print(f"{Colors.HEADER}└─────────────────────────────────────────────────────┘{Colors.ENDC}")
        
        # Delay giữa các lần chạy
        if i < total_runs - 1:
            delay = 5
            print(f"\n{Colors.WARNING}⏳ Waiting {delay}s for next account...{Colors.ENDC}\n")
            time.sleep(delay)

    print(f"\n{Colors.GREEN}{'='*60}")
    print(f"        ĐÃ HOÀN TẤT TOÀN BỘ CÔNG VIỆC. GOODBYE!")
    print(f"{'='*60}{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}[!] User Interrupt! Exiting...{Colors.ENDC}")
        sys.exit(0)
