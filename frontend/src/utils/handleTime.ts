export const dateFunction = (time: any) => {
  var zoneDate = new Date(time).toJSON();
  var date = new Date(+new Date(zoneDate) + 8 * 3600 * 1000)
    .toISOString()
    .replace(/T/g, " ")
    .replace(/\.[\d]{3}Z/, "");
  return date;
};
