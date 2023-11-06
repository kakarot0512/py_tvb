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
    一级:"js:var items=[];pdfh=jsp.pdfh;pdfa=jsp.pdfa;pd=jsp.pd;var html=request(input);var tabs=pdfa(html,'body&&.col-span-1');tabs.forEach(function(it){var pz=pdfh(it,'.space-x-2:eq(0)&&Text');var ps='国内转播';var pk=pdfh(it,'.space-x-2:eq(1)&&Text');var img=pd(it,'img&&src');var timer=pdfh(it,'.text-xs&&Text');var url=pd(it,'a&&href':eq(1));items.push({desc:timer+'🏆'+ps,title:pz+'🆚'+pk,pic_url:img,url:url})});setResult(items);",
    二级:{
        //"title":".sub_list li:lt(2)&&Text;.sub_list li:eq(0)&&Text",
        //"img":"img&&src",
        //"desc":";;;.lab_team_home&&Text;.lab_team_away&&Text",
        //"content":".sub_list ul&&Text",
        "tabs":"js:TABS=['咪咕腾讯']",
        //"lists":"js:lists=['mg$https://hlsmgsplive.miguvideo.com/migu/sports/20220127/pcstation39/57/01.m3u8?msisdn=d6a90faa9123d64d29c87f964ab3bd07&mdspid=&spid=800033&netType=4&sid=7510189347&pid=2029000099&timestamp=20231106080258&Channel_ID=0116_25000000-99000-100300010010001&ProgramID=881652858&ParentNodeID=-99&assertID=7510189347&client_ip=36.249.69.216&SecurityKey=20231106080258&promotionId=&mvid=7510094307&mcid=500020&mpid=120000487745&playurlVersion=WX-A1-6.11.1-RELEASE&userid=303687266&jmhm=d6a90faa9123d64d29c87f964ab3bd07&videocodec=h264&mtv_session=e7e9959b0e37b4254db6027bdb790c55&HlsSubType=1&HlsProfileId=1&nphaid=0&encrypt=ae1c324c4359381ae0bb04b4030fd6db']",
        "lists":"js:LISTS=[];pdfh=jsp.pdfh;pdfa=jsp.pdfa;pd=jsp.pd;let html=request(input);let data=pdfa(html,'.options&&.btn');TABS.forEach(function(tab){let d=data.map(function(it){let name=pdfh(it,'Text');let url=pd(it,'input&&value');return name+'$'+url});LISTS.push(d)});",
        },
    搜索:'',
}
