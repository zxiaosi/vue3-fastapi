import{h as e}from"./http.b52ceb59.js";let n="./student/";function a(t){return e.get(`${n}`,t)}function u(t){return e.get(`${n}${t}`)}function d(t){return e.post(`${n}`,t)}function o(t,r){return e.put(`${n}${t}`,r)}function s(t){return e.delete(`${n}${t}`)}function i(){return e.get(`${n}relation/`)}var c={read_datas:a,read_data:u,create_data:d,update_data:o,delete_data:s,student_relation:i};export{c as s};