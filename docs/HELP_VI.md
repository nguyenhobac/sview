# Hướng dẫn cài đặt và sử dụng sView (Tiếng Việt)

**sView** là phần mềm mã nguồn mở đa nền tảng dùng để xem ảnh và phát video lập thể 3D (Stereoscopic Media Player & Image Viewer), hỗ trợ nhiều định dạng 3D phổ biến (Side-by-Side, Over/Under, Anaglyph, Interlaced, PageFlip, VR/Panorama...).

---

## 1. Cài đặt

### 1.1. Cài đặt từ bản đóng gói trên macOS (`.zip` / `.app`)
1. Giải nén tệp `YYYYMMDD_HHMMSS_sview.zip` (hoặc lấy trực tiếp thư mục `YYYYMMDD_HHMMSS_sview.app` trong `dist/`).
2. Đổi tên thành `sView.app` (nếu muốn) và kéo vào thư mục **Applications** (`/Applications`).
3. Nếu macOS báo ứng dụng không thể mở do chưa ký chứng chỉ nhà phát triển (Gatekeeper), mở **Terminal** và chạy:
   ```bash
   xattr -cr /Applications/sView.app
   ```
   Sau đó mở lại ứng dụng bình thường.

### 1.2. Tự biên dịch (Build) từ mã nguồn trên macOS
#### Yêu cầu hệ thống
- **Xcode** đầy đủ (cần công cụ `ibtool` để biên dịch `MainMenu.xib`). Sau khi cài Xcode từ App Store, chạy:
  ```bash
  sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
  sudo xcodebuild -license accept
  ```
- **CMake**, **FreeType**, **FFmpeg** (có thể cài qua Homebrew):
  ```bash
  brew install cmake freetype ffmpeg openal-soft ninja
  ```

#### Các bước build tự động
Tại thư mục gốc dự án, chạy script Python:
```bash
python3 build_macos.py
```
Kết quả xuất ra nằm trong thư mục `dist/` theo định dạng thời gian:
- `dist/YYYYMMDD_HHMMSS_sview.app`
- `dist/YYYYMMDD_HHMMSS_sview.zip`

Một số tùy chọn hỗ trợ:
- `--clean`: Xóa thư mục `build/` và biên dịch lại từ đầu.
- `--no-zip`: Chỉ xuất `.app`, không nén `.zip`.
- `--dmg`: Đóng gói thêm tệp ảnh đĩa `.dmg`.
- `--build-type Debug`: Build bản Debug thay vì Release.

---

## 2. Chọn ngôn ngữ Tiếng Việt

1. Mở ứng dụng **sView**.
2. Trên thanh menu, chọn **Help → Language → Tiếng Việt** (hoặc **Trợ giúp → Ngôn ngữ → Tiếng Việt**).
3. Giao diện sẽ chuyển ngay sang Tiếng Việt.

---

## 3. Hướng dẫn sử dụng

### 3.1. Mở tệp và quản lý danh sách phát
- **Kéo & Thả (Drag & Drop)**: Kéo trực tiếp tệp ảnh hoặc video vào cửa sổ sView để mở.
- **Mở qua menu**:
  - Xem ảnh: **Tệp tin → Mở ảnh...** (`Ctrl + O`).
  - Xem video: **Tệp tin → Mở phim...** (`Ctrl + O`).
  - Hỗ trợ mở 1 tệp chứa cả 2 khung hình hoặc mở **Hai tệp Trái+Phải** riêng biệt.
- **Danh sách phát**: sView tự động nạp các tệp cùng thư mục hiện tại, hoặc bạn có thể mở tệp danh sách phát `.m3u`.

### 3.2. Thao tác chuột
- **Cuộn chuột / Trackpad**: Phóng to hoặc thu nhỏ tại vị trí con trỏ.
- **Nhấn giữ chuột trái + kéo**: Di chuyển vùng xem (Panning).
- **Nhấn nút chuột giữa**: Chuyển đổi Toàn màn hình / Cửa sổ.

### 3.3. Phím tắt thông dụng

#### Điều khiển chung & Điều hướng
| Phím tắt | Chức năng |
| :--- | :--- |
| `F` hoặc `Enter` | Chuyển Toàn màn hình / Cửa sổ |
| `Space` | Phát/Tạm dừng (Video) hoặc Bắt đầu/Dừng trình chiếu (Ảnh) |
| `Esc` | Thoát chương trình (tùy cấu hình trong Cài đặt) |
| `Ctrl + O` | Mở tệp mới |
| `Ctrl + S` | Lưu ảnh / Lưu ảnh chụp màn hình |
| `Ctrl + L` | Hiện/Ẩn danh sách phát |
| `Home` / `End` | Đến mục đầu tiên / cuối cùng trong danh sách phát |
| `Page Up` / `Page Down` | Mở mục trước / mục tiếp theo |
| `Left` / `Right` | Tua lùi / Tua tới 5 giây (Video) hoặc di chuyển trái/phải (Ảnh) |
| `Backspace` (`Delete` trên Mac) | Đặt lại vị trí hiển thị |

#### Chỉnh sửa ảnh & Xoay
| Phím tắt | Chức năng |
| :--- | :--- |
| `+` / `-` | Phóng to / Thu nhỏ |
| `[` / `]` | Xoay 90° ngược / cùng chiều kim đồng hồ |
| `Ctrl + [` / `Ctrl + ]` | Xoay mượt ngược / cùng chiều kim đồng hồ |
| `Shift + B` / `Ctrl + B` | Tăng / Giảm độ sáng |
| `Shift + G` / `Ctrl + G` | Tăng / Giảm Gamma |
| `Shift + T` / `Ctrl + T` | Tăng / Giảm độ bão hòa màu |

#### Chế độ 3D Stereoscopic & Panorama
| Phím tắt | Chức năng |
| :--- | :--- |
| `A` | Tự động nhận diện định dạng Stereo từ tệp |
| `M` | Chế độ Đơn (Mono 2D) |
| `S` | Định dạng Cạnh nhau (Side-by-Side) |
| `O` | Định dạng Trên/Dưới (Over/Under) |
| `W` | Đảo mắt Trái / Phải |
| `P` | Bật/Tắt chế độ Toàn cảnh (Panorama 360°) |
| `Numpad /` và `Numpad *` | Điều chỉnh tách ngang (thị sai) |
| `Ctrl + Numpad /` và `Ctrl + Numpad *` | Điều chỉnh tách dọc |

#### Âm thanh & Phụ đề (Trình phát phim)
| Phím tắt | Chức năng |
| :--- | :--- |
| `L` hoặc `H` | Chuyển rãnh âm thanh (Audio track) tiếp theo |
| `T` hoặc `U` | Chuyển rãnh phụ đề (Subtitle track) tiếp theo |

*(Lưu ý: Trên macOS, tổ hợp `Ctrl + ...` trong sView vẫn sử dụng phím `Control` hoặc có thể gán lại toàn bộ phím tắt trong mục **Trợ giúp → Phím tắt**).*

---

## 4. Tài liệu tham khảo thêm
- [User Tips (Tiếng Anh)](usertips.md)
- [Stereoscopic Formats (Tiếng Anh)](stereoformats.md)
- [FAQ (Tiếng Anh)](faq.md)
- [Install Guide (Tiếng Anh)](INSTALL.md)
