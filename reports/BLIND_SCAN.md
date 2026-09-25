# Quét độc lập trước khi xem pre-label

Frame: `frame_0182.jpg`

Số xe nhìn thấy bằng mắt: 26

Hai vị trí dễ bị AI bỏ sót hoặc vẽ sai, kèm mô tả xe: 
1. Xe nhỏ ở mép trái phía xa, gần đường chia làn, màu tối và kích thước nhỏ; dễ nhầm với bóng hoặc phần nền nên AI hay bỏ sót.
2. Một cặp xe ở giữa-giữa và gần mép phải, hai xe liền nhau trên cùng chiều xe, kích thước tương đối nhỏ và gần nhau; AI dễ vẽ sai hộp hoặc chỉ giữ một xe nếu không tách rõ ranh giới.

Chạy `python3 tools/lock_blind.py` ngay sau khi điền. Sau đó giữ file này nguyên vẹn.
