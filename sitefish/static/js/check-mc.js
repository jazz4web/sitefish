function getH() {
  let wh = $(window).height();
  let fh = $('#footer').height();
  let nh = $('#navigation').height();
  return wh - fh - nh;
}

function resize(wwidth, width, height) {
  if (wwidth > width) {
    $('#main-container').css({"width": 780,
                              "box-shadow": "0 0 10px #d3d3d3"});
  } else {
    $('#main-container').css({"width": wwidth - 20,
                              "box-shadow": "0 0 10px #d3d3d3"});
  }
}

function checkMC(width) {
  let wwidth = $(window).width();
  let mcon = $('#main-container');
  resize(wwidth, width);
  let height = getH();
  let mh = Math.round($('#main-container').height());
  if (height > mh) $('#main-container').css({"height": height - 2});
  $(window).on('resize', {mh: mh}, function(event) {
    let wwidth = $(window).width();
    resize(wwidth, width);
    let height = getH();
    if (height > event.data.mh) {
      $('#main-container').css({"height": height - 2});
    }
  });
}
