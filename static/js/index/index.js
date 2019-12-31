function load_page() {
    load_recommend();       // 推荐
    load_ranking_list();    // 排行榜
}

function load_recommend() {
    let url = "article/get_latest_article";
    $("#content").load(url, '');
}

function load_ranking_list() {
    let url = "article/get_ranking_list";
    $("#ms-main").load(url, '');
}
