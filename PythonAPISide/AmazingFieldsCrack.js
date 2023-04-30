var k = String.fromCharCode
              , F = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
              , N = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$"
              , b = {};
            function p(m, v) {
                if (!b[m]) {
                    b[m] = {};
                    for (var O = 0; O < m.length; O++)
                        b[m][m.charAt(O)] = O
                }
                return b[m][v]
            }
var f = {
                compressToBase64: function(m) {
                    if (null == m)
                        return "";
                    var v = f._compress(m, 6, function(O) {
                        return F.charAt(O)
                    });
                    switch (v.length % 4) {
                    default:
                    case 0:
                        return v;
                    case 1:
                        return v + "===";
                    case 2:
                        return v + "==";
                    case 3:
                        return v + "="
                    }
                },
                decompressFromBase64: function(m) {
                    return null == m ? "" : "" == m ? null : f._decompress(m.length, 32, function(v) {
                        return p(F, m.charAt(v))
                    })
                },
                compressToUTF16: function(m) {
                    return null == m ? "" : f._compress(m, 15, function(v) {
                        return k(v + 32)
                    }) + " "
                },
                decompressFromUTF16: function(m) {
                    return null == m ? "" : "" == m ? null : f._decompress(m.length, 16384, function(v) {
                        return m.charCodeAt(v) - 32
                    })
                },
                compressToUint8Array: function(m) {
                    for (var v = f.compress(m), O = new Uint8Array(2 * v.length), D = 0, x = v.length; D < x; D++) {
                        var M = v.charCodeAt(D);
                        O[2 * D] = M >>> 8,
                        O[2 * D + 1] = M % 256
                    }
                    return O
                },
                decompressFromUint8Array: function(m) {
                    if (null == m)
                        return f.decompress(m);
                    for (var v = new Array(m.length / 2), O = 0, D = v.length; O < D; O++)
                        v[O] = 256 * m[2 * O] + m[2 * O + 1];
                    var x = [];
                    return v.forEach(function(M) {
                        x.push(k(M))
                    }),
                    f.decompress(x.join(""))
                },
                compressToEncodedURIComponent: function(m) {
                    return null == m ? "" : f._compress(m, 6, function(v) {
                        return N.charAt(v)
                    })
                },
                decompressFromEncodedURIComponent: function(m) {
                    return null == m ? "" : "" == m ? null : (m = m.replace(/ /g, "+"),
                    f._decompress(m.length, 32, function(v) {
                        return p(N, m.charAt(v))
                    }))
                },
                compress: function(m) {
                    return f._compress(m, 16, function(v) {
                        return k(v)
                    })
                },
                _compress: function(m, v, O) {
                    if (null == m)
                        return "";
                    var D, x, je, M = {}, Q = {}, B = "", j = "", X = "", he = 2, H = 3, ie = 2, te = [], Ne = 0, _e = 0;
                    for (je = 0; je < m.length; je += 1)
                        if (B = m.charAt(je),
                        Object.prototype.hasOwnProperty.call(M, B) || (M[B] = H++,
                        Q[B] = !0),
                        j = X + B,
                        Object.prototype.hasOwnProperty.call(M, j))
                            X = j;
                        else {
                            if (Object.prototype.hasOwnProperty.call(Q, X)) {
                                if (X.charCodeAt(0) < 256) {
                                    for (D = 0; D < ie; D++)
                                        Ne <<= 1,
                                        _e == v - 1 ? (_e = 0,
                                        te.push(O(Ne)),
                                        Ne = 0) : _e++;
                                    for (x = X.charCodeAt(0),
                                    D = 0; D < 8; D++)
                                        Ne = Ne << 1 | 1 & x,
                                        _e == v - 1 ? (_e = 0,
                                        te.push(O(Ne)),
                                        Ne = 0) : _e++,
                                        x >>= 1
                                } else {
                                    for (x = 1,
                                    D = 0; D < ie; D++)
                                        Ne = Ne << 1 | x,
                                        _e == v - 1 ? (_e = 0,
                                        te.push(O(Ne)),
                                        Ne = 0) : _e++,
                                        x = 0;
                                    for (x = X.charCodeAt(0),
                                    D = 0; D < 16; D++)
                                        Ne = Ne << 1 | 1 & x,
                                        _e == v - 1 ? (_e = 0,
                                        te.push(O(Ne)),
                                        Ne = 0) : _e++,
                                        x >>= 1
                                }
                                0 == --he && (he = Math.pow(2, ie),
                                ie++),
                                delete Q[X]
                            } else
                                for (x = M[X],
                                D = 0; D < ie; D++)
                                    Ne = Ne << 1 | 1 & x,
                                    _e == v - 1 ? (_e = 0,
                                    te.push(O(Ne)),
                                    Ne = 0) : _e++,
                                    x >>= 1;
                            0 == --he && (he = Math.pow(2, ie),
                            ie++),
                            M[j] = H++,
                            X = String(B)
                        }
                    if ("" !== X) {
                        if (Object.prototype.hasOwnProperty.call(Q, X)) {
                            if (X.charCodeAt(0) < 256) {
                                for (D = 0; D < ie; D++)
                                    Ne <<= 1,
                                    _e == v - 1 ? (_e = 0,
                                    te.push(O(Ne)),
                                    Ne = 0) : _e++;
                                for (x = X.charCodeAt(0),
                                D = 0; D < 8; D++)
                                    Ne = Ne << 1 | 1 & x,
                                    _e == v - 1 ? (_e = 0,
                                    te.push(O(Ne)),
                                    Ne = 0) : _e++,
                                    x >>= 1
                            } else {
                                for (x = 1,
                                D = 0; D < ie; D++)
                                    Ne = Ne << 1 | x,
                                    _e == v - 1 ? (_e = 0,
                                    te.push(O(Ne)),
                                    Ne = 0) : _e++,
                                    x = 0;
                                for (x = X.charCodeAt(0),
                                D = 0; D < 16; D++)
                                    Ne = Ne << 1 | 1 & x,
                                    _e == v - 1 ? (_e = 0,
                                    te.push(O(Ne)),
                                    Ne = 0) : _e++,
                                    x >>= 1
                            }
                            0 == --he && (he = Math.pow(2, ie),
                            ie++),
                            delete Q[X]
                        } else
                            for (x = M[X],
                            D = 0; D < ie; D++)
                                Ne = Ne << 1 | 1 & x,
                                _e == v - 1 ? (_e = 0,
                                te.push(O(Ne)),
                                Ne = 0) : _e++,
                                x >>= 1;
                        0 == --he && (he = Math.pow(2, ie),
                        ie++)
                    }
                    for (x = 2,
                    D = 0; D < ie; D++)
                        Ne = Ne << 1 | 1 & x,
                        _e == v - 1 ? (_e = 0,
                        te.push(O(Ne)),
                        Ne = 0) : _e++,
                        x >>= 1;
                    for (; ; ) {
                        if (Ne <<= 1,
                        _e == v - 1) {
                            te.push(O(Ne));
                            break
                        }
                        _e++
                    }
                    return te.join("")
                },
                decompress: function(m) {
                    return null == m ? "" : "" == m ? null : f._decompress(m.length, 32768, function(v) {
                        return m.charCodeAt(v)
                    })
                },
                _decompress: function(m, v, O) {
                    var he, H, ie, te, Ne, _e, je, D = [], M = 4, Q = 4, B = 3, j = "", X = [], se = {
                        val: O(0),
                        position: v,
                        index: 1
                    };
                    for (he = 0; he < 3; he += 1)
                        D[he] = he;
                    for (ie = 0,
                    Ne = Math.pow(2, 2),
                    _e = 1; _e != Ne; )
                        te = se.val & se.position,
                        se.position >>= 1,
                        0 == se.position && (se.position = v,
                        se.val = O(se.index++)),
                        ie |= (te > 0 ? 1 : 0) * _e,
                        _e <<= 1;
                    switch (ie) {
                    case 0:
                        for (ie = 0,
                        Ne = Math.pow(2, 8),
                        _e = 1; _e != Ne; )
                            te = se.val & se.position,
                            se.position >>= 1,
                            0 == se.position && (se.position = v,
                            se.val = O(se.index++)),
                            ie |= (te > 0 ? 1 : 0) * _e,
                            _e <<= 1;
                        je = k(ie);
                        break;
                    case 1:
                        for (ie = 0,
                        Ne = Math.pow(2, 16),
                        _e = 1; _e != Ne; )
                            te = se.val & se.position,
                            se.position >>= 1,
                            0 == se.position && (se.position = v,
                            se.val = O(se.index++)),
                            ie |= (te > 0 ? 1 : 0) * _e,
                            _e <<= 1;
                        je = k(ie);
                        break;
                    case 2:
                        return ""
                    }
                    for (D[3] = je,
                    H = je,
                    X.push(je); ; ) {
                        if (se.index > m)
                            return "";
                        for (ie = 0,
                        Ne = Math.pow(2, B),
                        _e = 1; _e != Ne; )
                            te = se.val & se.position,
                            se.position >>= 1,
                            0 == se.position && (se.position = v,
                            se.val = O(se.index++)),
                            ie |= (te > 0 ? 1 : 0) * _e,
                            _e <<= 1;
                        switch (je = ie) {
                        case 0:
                            for (ie = 0,
                            Ne = Math.pow(2, 8),
                            _e = 1; _e != Ne; )
                                te = se.val & se.position,
                                se.position >>= 1,
                                0 == se.position && (se.position = v,
                                se.val = O(se.index++)),
                                ie |= (te > 0 ? 1 : 0) * _e,
                                _e <<= 1;
                            D[Q++] = k(ie),
                            je = Q - 1,
                            M--;
                            break;
                        case 1:
                            for (ie = 0,
                            Ne = Math.pow(2, 16),
                            _e = 1; _e != Ne; )
                                te = se.val & se.position,
                                se.position >>= 1,
                                0 == se.position && (se.position = v,
                                se.val = O(se.index++)),
                                ie |= (te > 0 ? 1 : 0) * _e,
                                _e <<= 1;
                            D[Q++] = k(ie),
                            je = Q - 1,
                            M--;
                            break;
                        case 2:
                            return X.join("")
                        }
                        if (0 == M && (M = Math.pow(2, B),
                        B++),
                        D[je])
                            j = D[je];
                        else {
                            if (je !== Q)
                                return null;
                            j = H + H.charAt(0)
                        }
                        X.push(j),
                        D[Q++] = H + j.charAt(0),
                        H = j,
                        0 == --M && (M = Math.pow(2, B),
                        B++)
                    }
                }
            };