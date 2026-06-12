# BÁO CÁO BÀI THỰC HÀNH SỐ 1

## PHẦN B – PHÂN TÍCH KẾT QUẢ KIỂM THỬ

*Giả định hàm `calculate_discount(total_amount)` chỉ đang nhận vào 1 biến là tổng giá trị trước đó.*

| TC | Tổng đơn hàng mua trước đây | Đơn hàng mới | Expected (Kỳ vọng) | Actual (Thực tế) | Status (Trạng thái) |
|---|---|---|---|---|---|
| **TC01** | 60M | 2M | 0.1 | 0.1 | **PASS** |
| **TC02** | 30M | 2M | 0 | 0 | **PASS** |
| **TC03** | 49M | 2M | 0.1 | 0 | **FAIL** |

*Giải thích cho TC03: Kỳ vọng là 0.1 (vì 49M + 2M = 51M >= 50M đủ điều kiện giảm giá). Tuy nhiên vì code cũ chỉ xét tổng trước đây (49M) nên trả về kết quả Thực tế là 0.*

---

## PHẦN C – CÂU HỎI THU HOẠCH

**1. Theo yêu cầu nghiệp vụ, khách hàng đạt ngưỡng 50 triệu ở thời điểm nào thì được giảm giá?**
> **Trả lời:** Theo yêu cầu số 3, khách hàng đạt ngưỡng 50 triệu ngay tại thời điểm thực hiện đơn hàng mới (tính tổng cả đơn hàng mới đó) thì đơn hàng mới đó cũng bắt đầu được hưởng giảm giá.

**2. Test case TC03 có ý nghĩa gì trong việc phát hiện lỗi?**
> **Trả lời:** TC03 là trường hợp "cận biên" (boundary) kiểm tra tình huống tổng giá trị mua hàng trước đó chưa đủ 50 triệu (chỉ 49 triệu), nhưng nếu tính thêm đơn hàng mới (2 triệu) thì tổng sẽ vượt qua mốc 50 triệu. Nó giúp phát hiện lỗi logic khi mã nguồn chỉ kiểm tra tổng mua hàng trước đây mà bỏ sót giá trị của đơn hàng hiện tại.

**3. Nếu chỉ viết 2 test case ban đầu thì bug có được phát hiện không? Vì sao?**
> **Trả lời:** **Không**. Vì 2 test case ban đầu chỉ kiểm tra trường hợp tổng đã lớn hơn hẳn 50 triệu (60 triệu) và trường hợp tổng còn kém rất xa (30 triệu). Cả hai test case này đều không bao quát được yêu cầu số 3 (cộng gộp đơn hàng mới làm thay đổi việc đạt mốc 50 triệu). Do đó, code sai vẫn pass 2 test case này.

**4. Bug xuất hiện ở đâu?**
> **Trả lời:** Bug xuất hiện ở file `discount.py` trong hàm `calculate_discount`.

**5. Dòng code nào gây ra bug?**
> **Trả lời:** Bug gây ra ở tham số hàm và câu lệnh điều kiện:
> `def calculate_discount(total_amount):`
> `if total_amount >= 50000000:`
> Nguyên nhân: Hàm đang thiếu một tham số (giá trị đơn hàng mới) và không thực hiện tính tổng hai giá trị lại với nhau trước khi xét điều kiện `\>= 50000000`.

**6. Yêu cầu nghiệp vụ nào đã bị hiểu sai?**
> **Trả lời:** **Yêu cầu nghiệp vụ thứ 3:** *"Khi khách hàng thực hiện đơn hàng mới làm cho tổng giá trị mua hàng trong năm đạt từ 50 triệu đồng trở lên thì đơn hàng đó cũng được hưởng giảm giá."* Lập trình viên đã hiểu sai thành chỉ kiểm tra **tổng giá trị mua hàng trong quá khứ** đã đạt 50 triệu hay chưa.

**7. Tại sao bug vẫn được push lên main?**
> **Trả lời:** Vì 2 Unit test ban đầu (`test_vip_customer`, `test_normal_customer`) vẫn trả về kết quả đúng (PASS). Lập trình viên chủ quan cho rằng khi Unit Test PASS 100% nghĩa là tính năng đã hoàn thiện và chính xác nên đã tiến hành commit và push lên nhánh `main`.

**8. Hoạt động nào trong quy trình phát triển phần mềm đáng lẽ phải phát hiện lỗi này sớm hơn?**
> **Trả lời:** Đáng lẽ lỗi này phải được phát hiện sớm trong các hoạt động:
> - **Thiết kế Unit Test (Test Design):** Cần phân tích giá trị biên và viết đủ các ca kiểm thử bám sát yêu cầu (đặc biệt là test case có sự cộng dồn 2 giá trị).
> - **Phân tích yêu cầu (Requirement Analysis) / Code Review:** Đội ngũ cần review chéo để làm rõ yêu cầu trước khi code, hoặc review code để thấy hàm bị thiếu tham số thứ 2.
