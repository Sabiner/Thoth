/**
 * 主页相关数据初始化加载
 */

function load_page() {
    load_recommend();           // 推荐
    load_ranking_list();        // 排行榜
    load_correlation_list();    // 相关列表
    load_all_tag();             // 获取所有标签
}

function load_recommend() {
    let url = "/article/get_latest_article";
    $("#content").load(url, "");
}

function load_ranking_list() {
    let url = "/article/get_ranking_list";
    $("#ms-main").load(url, "");
}

function load_correlation_list() {
    let url = "/article/get_correlation";
    $("#correlation").load(url, "");
}

function switch_tag(obj) {
    $("#topnav_current").removeAttr("id");
    $(obj).attr("id", "topnav_current");
}

/**
 * 关于我
 */
function about_me() {
    let url = "/about_me";
    $("article").load(url, "");
}

/**
 * 加载留言板界面
 */
function message_board() {
    $.ajax({
        type: "GET",
        url: "/guestbook/message_board",
        success: function (msg) {
            $("article").html(msg);
            load_guest_book();
        },
        error: function (XMLHttpRequest, textStatus, thrownError) {
        }
    });
}

/**
 * 归档
 */
function pigeonhole(tag_name="Python") {
    $.ajax({
        type: "GET",
        url: "/pigeonhole",
        success: function (msg) {
            $("article").html(msg);
            load_items_by_tag(tag_name);
        },
        error: function (XMLHttpRequest, textStatus, thrownError) {
        }
    });
}

/**
 * 留言
 */
function leave_word() {
    let message = $("textarea").val();
    $.ajax({
        type: 'POST',
        url: "/guestbook/leave_word",
        data: {
            message: message
        },
        success: function (data) {
            load_guest_book();
        },
        error: function (xhr, state, errorThrown) {
            console.log(errorThrown);
        }
    });
}

/**
 * 加载留言板最新内容
 */
function load_guest_book() {
    $.ajax({
        type: "GET",
        url: "/guestbook/load_guest_book",
        success: function (msg) {
            $("#guestbook").html(msg);
        },
        error: function (XMLHttpRequest, textStatus, thrownError) {
        }
    });
}

/**
 * 根据标签名称获取文章
 * @param tag_name 标签名称
 */
function load_items_by_tag(tag_name) {
    $.ajax({
        type: 'GET',
        url: "/pigeonhole/get_items_by_tag",
        data: {
            tag_name: tag_name
        },
        success: function (msg) {
            $("#items_by_tag").html(msg);
        },
        error: function (xhr, state, errorThrown) {
            console.log(errorThrown);
        }
    });
}

/**
 * 获取所有标签
 */
function load_all_tag() {
    $.ajax({
        type: 'GET',
        url: "/pigeonhole/get_all_tag",
        success: function (msg) {
            Object.keys(msg).forEach(function (i) {
                $("div.cloud ul").append("<a href=\"javascript: pigeonhole('" + i + "')\">" + i + "</a>")
            });
        },
        error: function (xhr, state, errorThrown) {
            console.log(errorThrown);
        }
    });
}
