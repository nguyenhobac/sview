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

## 4. Hướng dẫn từng nút bấm & menu trên giao diện

### 4.1. Thanh công cụ phía trên (Upper Toolbar)

Từ trái sang phải (góc trên bên trái):
1. **Mở tệp (Biểu tượng thư mục)**: Mở hộp thoại chọn tệp ảnh hoặc video để phát.
2. **Ảnh trước / Ảnh tiếp theo** *(chỉ có ở Trình xem ảnh)*: Chuyển nhanh sang ảnh trước hoặc ảnh kế tiếp trong thư mục/danh sách phát.
3. **Thông tin tệp (Biểu tượng chữ `i`)**: Hiển thị thông tin chi tiết của tệp đang mở (tên tệp, độ phân giải, định dạng điểm ảnh, hệ màu, thời lượng, thông số camera EXIF/JPS...).
4. **Định dạng lập thể nguồn (Biểu tượng 3D / Mono / SBS / OU)**: Nhấn để chọn nhanh bố cục 3D của tệp nguồn (*Tự động, Đơn Mono, Cạnh nhau Trái/Phải, Trên/Dưới...*).
5. **Đảo Trái/Phải (Biểu tượng 2 mũi tên đảo chiều)**: Hoán đổi khung hình mắt trái và mắt phải khi ảnh/video 3D bị ngược chiều sâu.
6. **Toàn cảnh / Panorama (Biểu tượng quả cầu/360°)**: Bật hoặc chọn nhanh chế độ chiếu toàn cảnh (*Hình cầu, Hình trụ, Cubemap, Bán cầu, Rạp chiếu phim...*).
7. **Chỉnh sửa ảnh (Biểu tượng bảng màu / thanh trượt)**: Bật/tắt bảng điều chỉnh nhanh **Độ sáng**, **Độ bão hòa** và **Gamma** (có nút **Khôi phục mặc định**).

Góc trên bên phải *(chỉ có ở Trình phát phim)*:
- **Chọn rãnh âm thanh (Biểu tượng loa/nốt nhạc)**: Chọn kênh âm thanh hoặc đính kèm tệp âm thanh ngoài.
- **Chọn rãnh phụ đề 1 & 2 (Biểu tượng `CC` / phụ đề)**: Chọn rãnh phụ đề chính/phụ hoặc đính kèm tệp phụ đề ngoài (`.srt`, `.ass`...).

### 4.2. Thanh công cụ phía dưới (Bottom Toolbar - Trình phát phim)

Từ trái sang phải:
- **Phát / Tạm dừng (Play/Pause)**: Bắt đầu hoặc tạm dừng phát video.
- **Thanh tiến trình (Seek Bar)**: Hiển thị thời gian phát; nhấp hoặc kéo để tua đến vị trí mong muốn.

Từ phải sang trái (góc dưới bên phải):
- **Toàn màn hình (Fullscreen)**: Chuyển đổi giữa chế độ cửa sổ và toàn màn hình.
- **Danh sách phát (Playlist)**: Hiện/ẩn bảng danh sách các tệp trong thư mục hiện tại.
- **Tệp tiếp theo / Tệp trước**: Chuyển sang video tiếp theo hoặc trước đó trong danh sách phát.
- **Thanh âm lượng & Nút Tắt/Bật tiếng (Mute)**: Kéo hoặc cuộn chuột trên thanh để tăng/giảm âm lượng; nhấn vào biểu tượng loa để tắt/bật tiếng nhanh.

### 4.3. Thanh Menu chính (Main Menu)

#### 1. **Tệp tin** (`Media`)
- **Mở ảnh... / Mở phim...**:
  - *Từ một tệp*: Mở 1 tệp ảnh hoặc video thông thường / 3D tích hợp.
  - *Hai tệp Trái+Phải*: Chọn riêng 2 tệp cho mắt trái và mắt phải.
- **Tệp gần đây** *(Trình phát phim)*: Mở nhanh các video đã xem gần đây hoặc chọn *Xóa lịch sử*.
- **Lưu ảnh thành... / Lưu ảnh chụp...**: Xuất ảnh đang xem hoặc chụp khung hình video hiện tại ra PNG/JPEG (áp dụng cả trạng thái đảo Trái/Phải hoặc chỉnh màu hiện tại).
- **Định dạng lập thể**: Chỉ định thủ công định dạng nguồn của tệp (*Theo nguồn, Đơn, Nhìn chéo, Cặp song song, Trên/Dưới P/T & T/P, Xen kẽ, Anaglyph, Tuần tự khung hình, 2 luồng...*).
- **Thông tin ảnh / Thông tin tệp**: Mở cửa sổ xem siêu dữ liệu và thông số kỹ thuật của tệp.
- **Phát ngẫu nhiên (Shuffle)**: Bật/tắt phát ngẫu nhiên trong danh sách phát.
- **Thiết bị âm thanh** *(Trình phát phim)*: Chọn thiết bị đầu ra âm thanh (loa, tai nghe, HDMI...).
- **Giải mã video trên GPU** *(Trình phát phim)*: Bật/tắt tăng tốc phần cứng khi giải mã video.
- **Giao diện Web** *(Trình phát phim)*: Điều khiển trình phát từ xa qua trình duyệt web (*Tắt / Khởi chạy một lần / Luôn khởi chạy*).
- **Thoát**: Đóng ứng dụng.

#### 2. **Hiển thị** (`View`)
- **Xuất Stereo**: Chọn cách hiển thị 3D ra màn hình (*Stereo, Chỉ mắt trái, Chỉ mắt phải, Cặp song song, Nhìn chéo*).
- **Toàn màn hình**: Bật/tắt chế độ toàn màn hình.
- **Đặt lại**: Đưa vị trí, thu phóng và góc xoay về mặc định.
- **Đảo Trái/Phải**: Hoán đổi hai mắt Trái/Phải.
- **Tỷ lệ hiển thị**: Chọn tỷ lệ khung hình (*Theo nguồn, Giữ khi khởi động lại, Sửa anamorphic 1080p/720p*).
- **Bộ lọc làm mịn**: Chọn thuật toán lọc điểm ảnh (*Gần nhất, Tuyến tính, Khử xen kẽ hòa trộn, Tam tuyến tính*).
- **Chỉnh sửa ảnh**: Mở bộ điều chỉnh *Độ sáng, Độ bão hòa, Gamma* và *Khôi phục mặc định*.
- **Toàn cảnh (Panorama)**: Chọn phép chiếu 360°/180° (*Tắt/Mặt phẳng, Hình cầu, Hình trụ, Cubemap, Bán cầu, Cubemap đẳng góc, Rạp chiếu phim*), bật *Theo dõi hướng* hoặc *Định hướng âm thanh*.

#### 3. **Âm thanh** *(chỉ có ở Trình phát phim)*
- Chọn rãnh âm thanh trong video hoặc chọn **Không có** để tắt tiếng.
- **Đính kèm từ tệp**: Nạp tệp âm thanh rời bên ngoài.
- **Độ trễ Âm thanh/Video**: Điều chỉnh đồng bộ tiếng và hình (nhập số giây dương nếu tiếng sớm hơn hình, số âm nếu tiếng chậm hơn hình).

#### 4. **Phụ đề** *(chỉ có ở Trình phát phim)*
- Chọn rãnh phụ đề có sẵn hoặc **Không có** để ẩn phụ đề.
- **Đính kèm từ tệp**: Nạp tệp phụ đề rời từ máy.
- **Cỡ chữ**: Thay đổi kích thước chữ phụ đề.
- **Thị sai (Parallax)**: Điều chỉnh độ nổi/sâu 3D của phụ đề khi xem phim lập thể.
- **Vị trí**: Đặt phụ đề ở *Trên cùng* hoặc *Dưới cùng*.
- **Trình phân tích văn bản**: Chọn *Văn bản thuần* hoặc *HTML đơn giản*.

#### 5. **Đổi thiết bị** (`Output`)
- Chọn mô-đun xuất 3D phù hợp với phần cứng: *Kính Anaglyph (Đỏ-Lục lam, Vàng-Xanh dương...), Màn hình xen kẽ, Xuất kép (Dual), Màn hình iZ3D, Kính màn trập (PageFlip), Xuất biến dạng / VR (OpenVR)...*
- **Giới thiệu plugin...**: Xem thông tin mô-đun xuất đang dùng.
- **Hiện FPS / Điều khiển FPS**: Bật bộ đếm khung hình/giây, bật/tắt **VSync**, **Giảm mức dùng CPU**, hoặc **Toàn màn hình độc quyền**.

#### 6. **Trợ giúp** (`Help`)
- **Giới thiệu...**: Xem phiên bản sView và thông tin tác giả.
- **Kiểm tra cập nhật**: Thiết lập tần suất kiểm tra bản mới (*Ngay bây giờ, Mỗi ngày, Mỗi tuần, Mỗi năm, Không bao giờ*).
- **Văn bản giấy phép**: Xem giấy phép mã nguồn mở GPL 3.0.
- **Ngôn ngữ**: Chuyển đổi ngôn ngữ giao diện (`Tiếng Việt`, `English`, ...).
- **Tỷ lệ giao diện**: Chọn kích thước nút và chữ giao diện (*Nhỏ, Bình thường, Lớn, Bắt buộc HiDPI 2X*).
- **Phím tắt**: Xem và gán lại phím tắt cho từng hành động.
- **Cài đặt**: Tùy chỉnh hành vi ứng dụng (*Thoát sView khi nhấn Esc, Mở tệp gần nhất khi khởi động, Đảo thứ tự khung hình JPS/PNS, Ưu tiên Deep Color 30-bit RGB, Chặn chế độ ngủ...*).
- **Thông tin hệ thống**: Xem thông tin OpenGL, GPU và bộ giải mã.
- **Mẹo sử dụng**: Mở hướng dẫn sử dụng nhanh.

---

## 5. Tài liệu tham khảo thêm
- [User Tips (Tiếng Anh)](usertips.md)
- [Stereoscopic Formats (Tiếng Anh)](stereoformats.md)
- [FAQ (Tiếng Anh)](faq.md)
- [Install Guide (Tiếng Anh)](INSTALL.md)

