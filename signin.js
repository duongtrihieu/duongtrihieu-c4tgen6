var signin_name = prompt("nhập vào tên đăng nhập của bạn: ");
var email = prompt("nhập vào email của bạn");
var password = prompt("nhập vào mật khẩu của bạn");
var password2 = prompt("nhập lại mật khảu của bạn");

if (password === password2) {
    console.log("tên đăng nhập: ",signin_name);
    console.log("mật khẩu: ",password);
    console.log("gmail: ",email);
}

else {
    console.log("mật khẩu ko khớp");
    console.log("yêu cầu nhập lại mật khẩu")
}