// Sabiner <chaoyue_ge@163.com>

$(function() {
    $("#get_tags").click(function () {
        url = "/load_tags_info";
        load_page(url);
    });
    $("#blog").click(function () {
        url = "/load_blog_page";
        load_page(url);
    });
});

layui.use('element', function(){
    var element = layui.element;
});

layui.use(['layer', 'form'], function () {
    var layer = layui.layer, form = layui.form;
});

function load_page(url) {
    $("#content").load(url, '');
}
