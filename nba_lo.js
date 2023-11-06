var rule = {
    title:'NBA_LiftOff',
    host:'https://www.chat-aigpt.vip',
    url:'/fyclass',
    searchUrl:'',
    searchable:0,
    quickSearch:0,
    class_name:'NBA',
    class_url:'/',
    //class_url:'?live',
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    timeout:5000,
    play_parse:true,
    lazy:"",
    limit:6,
    double:false,

     //是否启用辅助嗅探: 1,0
    sniffer:1,
    // 辅助嗅探规则
    推荐:'*',
    // 一级:'.loc_match:eq(2) ul;li:gt(1):lt(4)&&Text;img&&src;li:lt(2)&&Text;a:eq(1)&&href',//play.sportsteam333.com
    一级:"js:var items=[];pdfh=jsp.pdfh;pdfa=jsp.pdfa;pd=jsp.pd;var html=request(input);var tabs=pdfa(html,'body&&.col-span-1');tabs.forEach(function(it){var pz=pdfh(it,'.space-x-2:eq(0)&&Text');var ps='国内转播';var pk=pdfh(it,'.space-x-2:eq(1)&&Text');var img=pd(it,'img&&src');var timer=pdfh(it,'.text-xs&&Text');var url=pd(it,'a&&href');items.push({desc:timer+'🏆'+ps,title:pz+'🆚'+pk,pic_url:img,url:'https://www.chat-aigpt.vip/on_air/nbahdlive_g20231106cha@dal.php'})});setResult(items);",
    二级:{
        //"title":".sub_list li:lt(2)&&Text;.sub_list li:eq(0)&&Text",
        //"img":"img&&src",
        //"desc":";;;.lab_team_home&&Text;.lab_team_away&&Text",
        //"content":".sub_list ul&&Text",
        "tabs":"js:TABS=['咪咕','腾讯']",
        "lists":".btn&&value",
        //"lists":"js:LISTS=[];pdfh=jsp.pdfh;pdfa=jsp.pdfa;pd=jsp.pd;let html=request(input);let data=pdfa(html,'.sub_playlist&&a');TABS.forEach(function(tab){let d=data.map(function(it){let name=pdfh(it,'strong&&Text');let url=pd(it,'a&&data-play');return name+'$'+url});LISTS.push(d)});",
        },
    搜索:'',
}
