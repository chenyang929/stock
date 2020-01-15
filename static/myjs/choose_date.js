$(document).ready(function () {
    $(".layui-btn").click(function () {
        goLink($(this).attr("kind"), $("#date1").val());
    });
});

function goLink(n,d) {
    let url = "/search?" + "n=" + n + "&d=" + d;
    window.location.href = url;
}