function showTag(type_name) {
    var url = "/show_type?type=" + type_name;
    $("#content").load(url);
}
