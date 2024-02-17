function formatFooter(dt) {
  let footer = $.trim($('#footer-link').text());
  let html = '<span class="footer-link-text">' + footer +
    ', ' + dt.year + ' г.</span>';
  $('#footer-link').html(html);
}
