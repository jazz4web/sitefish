$(function() {
  let dt = luxon.DateTime.now();
  formatFooter(dt);
  checkMC(800);
  if ($('.today-field').length) renderTF('.today-field', dt);
});
