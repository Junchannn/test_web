var pay_status = 'Unpaid';

// Hàm kiểm tra trạng thái đơn hàng
// Sử dụng Ajax để lấy trạng thái đơn hàng. Nếu thanh toán thành công thì hiển thị Box đã thanh toán thành công, ẩn box checkout
function check_payment_status() {
    if (pay_status == 'Unpaid') {
        $.ajax({
            type: "POST",
            data: { order_id: 12345 }, // Replace 12345 with dynamic value as needed
            url: "https://payment-gateway-demo.sepay.dev/check_payment_status.php",
            dataType: "json",
            success: function (data) {
                if (data.payment_status == "Paid") {
                    $("#checkout_box").hide();
                    $("#success_pay_box").show();
                    pay_status = 'Paid';
                }
            }
        });
    }
}

// Kiểm tra trạng thái đơn hàng 1 giây một lần
setInterval(check_payment_status, 1000);
