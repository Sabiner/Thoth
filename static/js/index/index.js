/**
 * 主页相关数据初始化加载
 */

function load_page() {
    load_recommend();           // 推荐
    load_ranking_list();        // 排行榜
    load_correlation_list();    // 相关列表
}

function load_recommend() {
    let url = "article/get_latest_article";
    $("#content").load(url, "");
}

function load_ranking_list() {
    let url = "article/get_ranking_list";
    $("#ms-main").load(url, "");
}

function load_correlation_list() {
    let url = "article/get_correlation";
    $("#correlation").load(url, "");
}

function switch_tag(obj) {
    $("#topnav_current").removeAttr("id");
    $(obj).attr("id", "topnav_current");
}

function about_me() {
    let url = "about_me";
    $("article").load(url, "");
}