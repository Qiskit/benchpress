OPENQASM 2.0;
include "qelib1.inc";
qreg q[84];
ry(pi/2) q[0];
rx(pi) q[0];
ry(pi/2) q[1];
rx(pi) q[1];
cx q[0],q[1];
rz(0.42920412547152276) q[1];
cx q[0],q[1];
ry(pi/2) q[2];
rx(pi) q[2];
cx q[0],q[2];
rz(0.42920412547152276) q[2];
cx q[0],q[2];
rx(9.517239446365442) q[2];
ry(pi/2) q[3];
rx(pi) q[3];
cx q[0],q[3];
rz(0.42920412547152276) q[3];
cx q[0],q[3];
cx q[1],q[3];
rz(0.42920412547152276) q[3];
cx q[1],q[3];
ry(pi/2) q[4];
rx(pi) q[4];
cx q[1],q[4];
rz(0.42920412547152276) q[4];
cx q[1],q[4];
cx q[3],q[4];
rz(0.42920412547152276) q[4];
cx q[3],q[4];
ry(pi/2) q[5];
rx(pi) q[5];
cx q[1],q[5];
rz(0.42920412547152276) q[5];
cx q[1],q[5];
cx q[3],q[5];
rz(0.42920412547152276) q[5];
cx q[3],q[5];
ry(pi/2) q[6];
rx(pi) q[6];
cx q[4],q[6];
rz(0.42920412547152276) q[6];
cx q[4],q[6];
cx q[5],q[6];
rz(0.42920412547152276) q[6];
cx q[5],q[6];
ry(pi/2) q[7];
rx(pi) q[7];
cx q[3],q[7];
rz(0.42920412547152276) q[7];
cx q[3],q[7];
cx q[4],q[7];
rz(0.42920412547152276) q[7];
cx q[4],q[7];
ry(pi/2) q[8];
rx(pi) q[8];
cx q[3],q[8];
rz(0.42920412547152276) q[8];
cx q[3],q[8];
cx q[5],q[8];
rz(0.42920412547152276) q[8];
cx q[5],q[8];
ry(pi/2) q[9];
rx(pi) q[9];
cx q[1],q[9];
rz(0.42920412547152276) q[9];
cx q[1],q[9];
cx q[3],q[9];
rz(0.42920412547152276) q[9];
cx q[3],q[9];
ry(pi/2) q[10];
rx(pi) q[10];
cx q[4],q[10];
rz(0.42920412547152276) q[10];
cx q[4],q[10];
cx q[6],q[10];
rz(0.42920412547152276) q[10];
cx q[6],q[10];
ry(pi/2) q[11];
rx(pi) q[11];
cx q[5],q[11];
rz(0.42920412547152276) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(0.42920412547152276) q[11];
cx q[6],q[11];
rx(9.517239446365442) q[11];
ry(pi/2) q[12];
rx(pi) q[12];
cx q[3],q[12];
rz(0.42920412547152276) q[12];
cx q[3],q[12];
cx q[5],q[12];
rz(0.42920412547152276) q[12];
cx q[5],q[12];
ry(pi/2) q[13];
rx(pi) q[13];
cx q[4],q[13];
rz(0.42920412547152276) q[13];
cx q[4],q[13];
cx q[5],q[13];
rz(0.42920412547152276) q[13];
cx q[5],q[13];
ry(pi/2) q[14];
rx(pi) q[14];
cx q[3],q[14];
rz(0.42920412547152276) q[14];
cx q[3],q[14];
cx q[4],q[14];
rz(0.42920412547152276) q[14];
cx q[4],q[14];
rx(9.517239446365442) q[14];
ry(pi/2) q[15];
rx(pi) q[15];
cx q[0],q[15];
rz(0.42920412547152276) q[15];
cx q[0],q[15];
cx q[3],q[15];
rz(0.42920412547152276) q[15];
cx q[3],q[15];
ry(pi/2) q[16];
rx(pi) q[16];
cx q[0],q[16];
rz(0.42920412547152276) q[16];
cx q[0],q[16];
cx q[3],q[16];
rz(0.42920412547152276) q[16];
cx q[3],q[16];
ry(pi/2) q[17];
rx(pi) q[17];
cx q[1],q[17];
rz(0.42920412547152276) q[17];
cx q[1],q[17];
cx q[3],q[17];
rz(0.42920412547152276) q[17];
cx q[3],q[17];
ry(pi/2) q[18];
rx(pi) q[18];
cx q[3],q[18];
rz(0.42920412547152276) q[18];
cx q[3],q[18];
cx q[4],q[18];
rz(0.42920412547152276) q[18];
cx q[4],q[18];
ry(pi/2) q[19];
rx(pi) q[19];
cx q[3],q[19];
rz(0.42920412547152276) q[19];
cx q[3],q[19];
cx q[7],q[19];
rz(0.42920412547152276) q[19];
cx q[7],q[19];
ry(pi/2) q[20];
rx(pi) q[20];
cx q[0],q[20];
rz(0.42920412547152276) q[20];
cx q[0],q[20];
cx q[15],q[20];
rz(0.42920412547152276) q[20];
cx q[15],q[20];
ry(pi/2) q[21];
rx(pi) q[21];
cx q[4],q[21];
rz(0.42920412547152276) q[21];
cx q[4],q[21];
cx q[15],q[21];
rz(0.42920412547152276) q[21];
cx q[15],q[21];
ry(pi/2) q[22];
rx(pi) q[22];
cx q[3],q[22];
rz(0.42920412547152276) q[22];
cx q[3],q[22];
cx q[9],q[22];
rz(0.42920412547152276) q[22];
cx q[9],q[22];
rx(9.517239446365442) q[22];
ry(pi/2) q[23];
rx(pi) q[23];
cx q[3],q[23];
rz(0.42920412547152276) q[23];
cx q[3],q[23];
cx q[17],q[23];
rz(0.42920412547152276) q[23];
cx q[17],q[23];
ry(pi/2) q[24];
rx(pi) q[24];
cx q[3],q[24];
rz(0.42920412547152276) q[24];
cx q[3],q[24];
cx q[5],q[24];
rz(0.42920412547152276) q[24];
cx q[5],q[24];
ry(pi/2) q[25];
rx(pi) q[25];
cx q[3],q[25];
rz(0.42920412547152276) q[25];
cx q[3],q[25];
cx q[12],q[25];
rz(0.42920412547152276) q[25];
cx q[12],q[25];
rx(9.517239446365442) q[25];
ry(pi/2) q[26];
rx(pi) q[26];
cx q[3],q[26];
rz(0.42920412547152276) q[26];
cx q[3],q[26];
cx q[21],q[26];
rz(0.42920412547152276) q[26];
cx q[21],q[26];
ry(pi/2) q[27];
rx(pi) q[27];
cx q[4],q[27];
rz(0.42920412547152276) q[27];
cx q[4],q[27];
cx q[6],q[27];
rz(0.42920412547152276) q[27];
cx q[6],q[27];
ry(pi/2) q[28];
rx(pi) q[28];
cx q[1],q[28];
rz(0.42920412547152276) q[28];
cx q[1],q[28];
cx q[3],q[28];
rz(0.42920412547152276) q[28];
cx q[3],q[28];
ry(pi/2) q[29];
rx(pi) q[29];
cx q[1],q[29];
rz(0.42920412547152276) q[29];
cx q[1],q[29];
cx q[3],q[29];
rz(0.42920412547152276) q[29];
cx q[3],q[29];
rx(9.517239446365442) q[29];
ry(pi/2) q[30];
rx(pi) q[30];
cx q[3],q[30];
rz(0.42920412547152276) q[30];
cx q[3],q[30];
cx q[18],q[30];
rz(0.42920412547152276) q[30];
cx q[18],q[30];
rx(9.517239446365442) q[18];
ry(pi/2) q[31];
rx(pi) q[31];
cx q[12],q[31];
rz(0.42920412547152276) q[31];
cx q[12],q[31];
cx q[26],q[31];
rz(0.42920412547152276) q[31];
cx q[26],q[31];
rx(9.517239446365442) q[26];
rx(9.517239446365442) q[31];
ry(pi/2) q[32];
rx(pi) q[32];
cx q[0],q[32];
rz(0.42920412547152276) q[32];
cx q[0],q[32];
cx q[21],q[32];
rz(0.42920412547152276) q[32];
cx q[21],q[32];
ry(pi/2) q[33];
rx(pi) q[33];
cx q[5],q[33];
rz(0.42920412547152276) q[33];
cx q[5],q[33];
cx q[30],q[33];
rz(0.42920412547152276) q[33];
cx q[30],q[33];
rx(9.517239446365442) q[33];
ry(pi/2) q[34];
rx(pi) q[34];
cx q[3],q[34];
rz(0.42920412547152276) q[34];
cx q[3],q[34];
cx q[12],q[34];
rz(0.42920412547152276) q[34];
cx q[12],q[34];
ry(pi/2) q[35];
rx(pi) q[35];
cx q[3],q[35];
rz(0.42920412547152276) q[35];
cx q[3],q[35];
cx q[32],q[35];
rz(0.42920412547152276) q[35];
cx q[32],q[35];
rx(9.517239446365442) q[35];
ry(pi/2) q[36];
rx(pi) q[36];
cx q[15],q[36];
rz(0.42920412547152276) q[36];
cx q[15],q[36];
cx q[20],q[36];
rz(0.42920412547152276) q[36];
cx q[20],q[36];
rx(9.517239446365442) q[36];
ry(pi/2) q[37];
rx(pi) q[37];
cx q[10],q[37];
rz(0.42920412547152276) q[37];
cx q[10],q[37];
cx q[34],q[37];
rz(0.42920412547152276) q[37];
cx q[34],q[37];
rx(9.517239446365442) q[34];
rx(9.517239446365442) q[37];
ry(pi/2) q[38];
rx(pi) q[38];
cx q[19],q[38];
rz(0.42920412547152276) q[38];
cx q[19],q[38];
rx(9.517239446365442) q[19];
cx q[21],q[38];
rz(0.42920412547152276) q[38];
cx q[21],q[38];
ry(pi/2) q[39];
rx(pi) q[39];
cx q[3],q[39];
rz(0.42920412547152276) q[39];
cx q[3],q[39];
cx q[13],q[39];
rz(0.42920412547152276) q[39];
cx q[13],q[39];
rx(9.517239446365442) q[39];
ry(pi/2) q[40];
rx(pi) q[40];
cx q[3],q[40];
rz(0.42920412547152276) q[40];
cx q[3],q[40];
cx q[23],q[40];
rz(0.42920412547152276) q[40];
cx q[23],q[40];
rx(9.517239446365442) q[40];
ry(pi/2) q[41];
rx(pi) q[41];
cx q[10],q[41];
rz(0.42920412547152276) q[41];
cx q[10],q[41];
cx q[27],q[41];
rz(0.42920412547152276) q[41];
cx q[27],q[41];
ry(pi/2) q[42];
rx(pi) q[42];
cx q[0],q[42];
rz(0.42920412547152276) q[42];
cx q[0],q[42];
cx q[3],q[42];
rz(0.42920412547152276) q[42];
cx q[3],q[42];
ry(pi/2) q[43];
rx(pi) q[43];
cx q[3],q[43];
rz(0.42920412547152276) q[43];
cx q[3],q[43];
cx q[20],q[43];
rz(0.42920412547152276) q[43];
cx q[20],q[43];
rx(9.517239446365442) q[20];
rx(9.517239446365442) q[43];
ry(pi/2) q[44];
rx(pi) q[44];
cx q[3],q[44];
rz(0.42920412547152276) q[44];
cx q[3],q[44];
cx q[12],q[44];
rz(0.42920412547152276) q[44];
cx q[12],q[44];
ry(pi/2) q[45];
rx(pi) q[45];
cx q[1],q[45];
rz(0.42920412547152276) q[45];
cx q[1],q[45];
cx q[16],q[45];
rz(0.42920412547152276) q[45];
cx q[16],q[45];
ry(pi/2) q[46];
rx(pi) q[46];
cx q[5],q[46];
rz(0.42920412547152276) q[46];
cx q[5],q[46];
cx q[38],q[46];
rz(0.42920412547152276) q[46];
cx q[38],q[46];
rx(9.517239446365442) q[38];
rx(9.517239446365442) q[46];
ry(pi/2) q[47];
rx(pi) q[47];
cx q[4],q[47];
rz(0.42920412547152276) q[47];
cx q[4],q[47];
cx q[17],q[47];
rz(0.42920412547152276) q[47];
cx q[17],q[47];
ry(pi/2) q[48];
rx(pi) q[48];
cx q[0],q[48];
rz(0.42920412547152276) q[48];
cx q[0],q[48];
cx q[30],q[48];
rz(0.42920412547152276) q[48];
cx q[30],q[48];
rx(9.517239446365442) q[48];
ry(pi/2) q[49];
rx(pi) q[49];
cx q[3],q[49];
rz(0.42920412547152276) q[49];
cx q[3],q[49];
cx q[4],q[49];
rz(0.42920412547152276) q[49];
cx q[4],q[49];
rx(9.517239446365442) q[49];
ry(pi/2) q[50];
rx(pi) q[50];
cx q[3],q[50];
rz(0.42920412547152276) q[50];
cx q[3],q[50];
cx q[12],q[50];
rz(0.42920412547152276) q[50];
cx q[12],q[50];
ry(pi/2) q[51];
rx(pi) q[51];
cx q[0],q[51];
rz(0.42920412547152276) q[51];
cx q[0],q[51];
cx q[28],q[51];
rz(0.42920412547152276) q[51];
cx q[28],q[51];
rx(9.517239446365442) q[51];
ry(pi/2) q[52];
rx(pi) q[52];
cx q[3],q[52];
rz(0.42920412547152276) q[52];
cx q[3],q[52];
cx q[10],q[52];
rz(0.42920412547152276) q[52];
cx q[10],q[52];
rx(9.517239446365442) q[52];
ry(pi/2) q[53];
rx(pi) q[53];
cx q[17],q[53];
rz(0.42920412547152276) q[53];
cx q[17],q[53];
cx q[21],q[53];
rz(0.42920412547152276) q[53];
cx q[21],q[53];
ry(pi/2) q[54];
rx(pi) q[54];
cx q[24],q[54];
rz(0.42920412547152276) q[54];
cx q[24],q[54];
cx q[28],q[54];
rz(0.42920412547152276) q[54];
cx q[28],q[54];
rx(9.517239446365442) q[54];
ry(pi/2) q[55];
rx(pi) q[55];
cx q[9],q[55];
rz(0.42920412547152276) q[55];
cx q[9],q[55];
cx q[15],q[55];
rz(0.42920412547152276) q[55];
cx q[15],q[55];
rx(9.517239446365442) q[55];
ry(pi/2) q[56];
rx(pi) q[56];
cx q[13],q[56];
rz(0.42920412547152276) q[56];
cx q[13],q[56];
cx q[45],q[56];
rz(0.42920412547152276) q[56];
cx q[45],q[56];
rx(9.517239446365442) q[45];
ry(pi/2) q[57];
rx(pi) q[57];
cx q[1],q[57];
rz(0.42920412547152276) q[57];
cx q[1],q[57];
cx q[3],q[57];
rz(0.42920412547152276) q[57];
cx q[3],q[57];
rx(9.517239446365442) q[57];
ry(pi/2) q[58];
rx(pi) q[58];
cx q[24],q[58];
rz(0.42920412547152276) q[58];
cx q[24],q[58];
rx(9.517239446365442) q[24];
cx q[28],q[58];
rz(0.42920412547152276) q[58];
cx q[28],q[58];
rx(9.517239446365442) q[28];
rx(9.517239446365442) q[58];
ry(pi/2) q[59];
rx(pi) q[59];
cx q[16],q[59];
rz(0.42920412547152276) q[59];
cx q[16],q[59];
cx q[32],q[59];
rz(0.42920412547152276) q[59];
cx q[32],q[59];
ry(pi/2) q[60];
rx(pi) q[60];
cx q[1],q[60];
rz(0.42920412547152276) q[60];
cx q[1],q[60];
rx(9.517239446365442) q[1];
cx q[7],q[60];
rz(0.42920412547152276) q[60];
cx q[7],q[60];
ry(pi/2) q[61];
rx(pi) q[61];
cx q[4],q[61];
rz(0.42920412547152276) q[61];
cx q[4],q[61];
rx(9.517239446365442) q[4];
cx q[7],q[61];
rz(0.42920412547152276) q[61];
cx q[7],q[61];
rx(9.517239446365442) q[7];
rx(9.517239446365442) q[61];
ry(pi/2) q[62];
rx(pi) q[62];
cx q[0],q[62];
rz(0.42920412547152276) q[62];
cx q[0],q[62];
cx q[17],q[62];
rz(0.42920412547152276) q[62];
cx q[17],q[62];
rx(9.517239446365442) q[62];
ry(pi/2) q[63];
rx(pi) q[63];
cx q[12],q[63];
rz(0.42920412547152276) q[63];
cx q[12],q[63];
rx(9.517239446365442) q[12];
cx q[17],q[63];
rz(0.42920412547152276) q[63];
cx q[17],q[63];
ry(pi/2) q[64];
rx(pi) q[64];
cx q[0],q[64];
rz(0.42920412547152276) q[64];
cx q[0],q[64];
cx q[10],q[64];
rz(0.42920412547152276) q[64];
cx q[10],q[64];
rx(9.517239446365442) q[10];
rx(9.517239446365442) q[64];
ry(pi/2) q[65];
rx(pi) q[65];
cx q[5],q[65];
rz(0.42920412547152276) q[65];
cx q[5],q[65];
cx q[23],q[65];
rz(0.42920412547152276) q[65];
cx q[23],q[65];
rx(9.517239446365442) q[23];
rx(9.517239446365442) q[65];
ry(pi/2) q[66];
rx(pi) q[66];
cx q[17],q[66];
rz(0.42920412547152276) q[66];
cx q[17],q[66];
rx(9.517239446365442) q[17];
cx q[47],q[66];
rz(0.42920412547152276) q[66];
cx q[47],q[66];
rx(9.517239446365442) q[47];
rx(9.517239446365442) q[66];
ry(pi/2) q[67];
rx(pi) q[67];
cx q[41],q[67];
rz(0.42920412547152276) q[67];
cx q[41],q[67];
rx(9.517239446365442) q[41];
cx q[56],q[67];
rz(0.42920412547152276) q[67];
cx q[56],q[67];
rx(9.517239446365442) q[67];
ry(pi/2) q[68];
rx(pi) q[68];
cx q[13],q[68];
rz(0.42920412547152276) q[68];
cx q[13],q[68];
rx(9.517239446365442) q[13];
cx q[32],q[68];
rz(0.42920412547152276) q[68];
cx q[32],q[68];
rx(9.517239446365442) q[32];
ry(pi/2) q[69];
rx(pi) q[69];
cx q[6],q[69];
rz(0.42920412547152276) q[69];
cx q[6],q[69];
cx q[59],q[69];
rz(0.42920412547152276) q[69];
cx q[59],q[69];
rx(9.517239446365442) q[69];
ry(pi/2) q[70];
rx(pi) q[70];
cx q[3],q[70];
rz(0.42920412547152276) q[70];
cx q[3],q[70];
cx q[15],q[70];
rz(0.42920412547152276) q[70];
cx q[15],q[70];
rx(9.517239446365442) q[70];
ry(pi/2) q[71];
rx(pi) q[71];
cx q[3],q[71];
rz(0.42920412547152276) q[71];
cx q[3],q[71];
cx q[53],q[71];
rz(0.42920412547152276) q[71];
cx q[53],q[71];
rx(9.517239446365442) q[53];
rx(9.517239446365442) q[71];
ry(pi/2) q[72];
rx(pi) q[72];
cx q[27],q[72];
rz(0.42920412547152276) q[72];
cx q[27],q[72];
rx(9.517239446365442) q[27];
cx q[44],q[72];
rz(0.42920412547152276) q[72];
cx q[44],q[72];
rx(9.517239446365442) q[44];
rx(9.517239446365442) q[72];
ry(pi/2) q[73];
rx(pi) q[73];
cx q[16],q[73];
rz(0.42920412547152276) q[73];
cx q[16],q[73];
rx(9.517239446365442) q[16];
cx q[59],q[73];
rz(0.42920412547152276) q[73];
cx q[59],q[73];
rx(9.517239446365442) q[59];
rx(9.517239446365442) q[73];
ry(pi/2) q[74];
rx(pi) q[74];
cx q[56],q[74];
rz(0.42920412547152276) q[74];
cx q[56],q[74];
cx q[63],q[74];
rz(0.42920412547152276) q[74];
cx q[63],q[74];
rx(9.517239446365442) q[63];
rx(9.517239446365442) q[74];
ry(pi/2) q[75];
rx(pi) q[75];
cx q[0],q[75];
rz(0.42920412547152276) q[75];
cx q[0],q[75];
cx q[21],q[75];
rz(0.42920412547152276) q[75];
cx q[21],q[75];
rx(9.517239446365442) q[75];
ry(pi/2) q[76];
rx(pi) q[76];
cx q[5],q[76];
rz(0.42920412547152276) q[76];
cx q[5],q[76];
rx(9.517239446365442) q[5];
cx q[6],q[76];
rz(0.42920412547152276) q[76];
cx q[6],q[76];
rx(9.517239446365442) q[76];
ry(pi/2) q[77];
rx(pi) q[77];
cx q[3],q[77];
rz(0.42920412547152276) q[77];
cx q[3],q[77];
rx(9.517239446365442) q[3];
cx q[30],q[77];
rz(0.42920412547152276) q[77];
cx q[30],q[77];
rx(9.517239446365442) q[30];
ry(pi/2) q[78];
rx(pi) q[78];
cx q[42],q[78];
rz(0.42920412547152276) q[78];
cx q[42],q[78];
rx(9.517239446365442) q[42];
cx q[60],q[78];
rz(0.42920412547152276) q[78];
cx q[60],q[78];
rx(9.517239446365442) q[60];
rx(9.517239446365442) q[78];
ry(pi/2) q[79];
rx(pi) q[79];
cx q[6],q[79];
rz(0.42920412547152276) q[79];
cx q[6],q[79];
rx(9.517239446365442) q[6];
cx q[50],q[79];
rz(0.42920412547152276) q[79];
cx q[50],q[79];
rx(9.517239446365442) q[50];
rx(9.517239446365442) q[79];
ry(pi/2) q[80];
rx(pi) q[80];
cx q[9],q[80];
rz(0.42920412547152276) q[80];
cx q[9],q[80];
rx(9.517239446365442) q[9];
cx q[15],q[80];
rz(0.42920412547152276) q[80];
cx q[15],q[80];
rx(9.517239446365442) q[15];
rx(9.517239446365442) q[80];
ry(pi/2) q[81];
rx(pi) q[81];
cx q[21],q[81];
rz(0.42920412547152276) q[81];
cx q[21],q[81];
rx(9.517239446365442) q[21];
cx q[77],q[81];
rz(0.42920412547152276) q[81];
cx q[77],q[81];
rx(9.517239446365442) q[77];
rx(9.517239446365442) q[81];
ry(pi/2) q[82];
rx(pi) q[82];
cx q[0],q[82];
rz(0.42920412547152276) q[82];
cx q[0],q[82];
rx(9.517239446365442) q[0];
cx q[0],q[1];
rz(4.581677159839479) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(4.581677159839479) q[2];
cx q[0],q[2];
cx q[0],q[3];
rx(3.136542363820505) q[2];
rz(4.581677159839479) q[3];
cx q[0],q[3];
cx q[0],q[15];
cx q[1],q[3];
rz(4.581677159839479) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(4.581677159839479) q[4];
cx q[1],q[4];
cx q[1],q[5];
cx q[3],q[4];
rz(4.581677159839479) q[4];
cx q[3],q[4];
cx q[4],q[6];
rz(4.581677159839479) q[5];
cx q[1],q[5];
cx q[1],q[9];
cx q[3],q[5];
rz(4.581677159839479) q[5];
cx q[3],q[5];
cx q[3],q[7];
rz(4.581677159839479) q[6];
cx q[4],q[6];
cx q[5],q[6];
rz(4.581677159839479) q[6];
cx q[5],q[6];
rz(4.581677159839479) q[7];
cx q[3],q[7];
cx q[4],q[7];
rz(4.581677159839479) q[7];
cx q[4],q[7];
cx q[4],q[10];
rz(4.581677159839479) q[9];
cx q[1],q[9];
cx q[1],q[17];
rz(4.581677159839479) q[10];
cx q[4],q[10];
cx q[4],q[13];
cx q[6],q[10];
rz(4.581677159839479) q[10];
cx q[6],q[10];
cx q[10],q[37];
rz(4.581677159839479) q[13];
cx q[4],q[13];
rz(4.581677159839479) q[15];
cx q[0],q[15];
cx q[0],q[16];
rz(4.581677159839479) q[16];
cx q[0],q[16];
cx q[0],q[20];
rz(4.581677159839479) q[17];
cx q[1],q[17];
cx q[1],q[28];
rz(4.581677159839479) q[20];
cx q[0],q[20];
cx q[0],q[32];
rz(4.581677159839479) q[28];
cx q[1],q[28];
cx q[1],q[29];
rz(4.581677159839479) q[29];
cx q[1],q[29];
cx q[1],q[45];
rz(4.581677159839479) q[32];
cx q[0],q[32];
cx q[0],q[42];
rz(4.581677159839479) q[37];
cx q[10],q[37];
cx q[10],q[41];
rz(4.581677159839479) q[41];
cx q[10],q[41];
rz(4.581677159839479) q[42];
cx q[0],q[42];
cx q[0],q[48];
rz(4.581677159839479) q[45];
cx q[1],q[45];
cx q[1],q[57];
rz(4.581677159839479) q[48];
cx q[0],q[48];
cx q[0],q[51];
rz(4.581677159839479) q[51];
cx q[0],q[51];
cx q[0],q[62];
cx q[56],q[82];
rz(4.581677159839479) q[57];
cx q[1],q[57];
cx q[1],q[60];
rz(4.581677159839479) q[60];
cx q[1],q[60];
rx(3.136542363820505) q[1];
rz(4.581677159839479) q[62];
cx q[0],q[62];
cx q[0],q[64];
rz(4.581677159839479) q[64];
cx q[0],q[64];
cx q[0],q[75];
rz(4.581677159839479) q[75];
cx q[0],q[75];
rz(0.42920412547152276) q[82];
cx q[56],q[82];
rx(9.517239446365442) q[56];
rx(9.517239446365442) q[82];
cx q[0],q[82];
rz(4.581677159839479) q[82];
cx q[0],q[82];
rx(3.136542363820505) q[0];
cx q[0],q[1];
rz(5.439121417687856) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(5.439121417687856) q[2];
cx q[0],q[2];
rx(6.767686082016463) q[2];
ry(pi/2) q[83];
rx(pi) q[83];
cx q[8],q[83];
rz(0.42920412547152276) q[83];
cx q[8],q[83];
rx(9.517239446365442) q[8];
cx q[3],q[8];
rz(4.581677159839479) q[8];
cx q[3],q[8];
cx q[3],q[9];
cx q[5],q[8];
rz(4.581677159839479) q[8];
cx q[5],q[8];
cx q[5],q[11];
rz(4.581677159839479) q[9];
cx q[3],q[9];
cx q[3],q[12];
rz(4.581677159839479) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(4.581677159839479) q[11];
cx q[6],q[11];
rx(3.136542363820505) q[11];
rz(4.581677159839479) q[12];
cx q[3],q[12];
cx q[3],q[14];
cx q[5],q[12];
rz(4.581677159839479) q[12];
cx q[5],q[12];
cx q[5],q[13];
rz(4.581677159839479) q[13];
cx q[5],q[13];
rz(4.581677159839479) q[14];
cx q[3],q[14];
cx q[3],q[15];
cx q[4],q[14];
rz(4.581677159839479) q[14];
cx q[4],q[14];
rx(3.136542363820505) q[14];
rz(4.581677159839479) q[15];
cx q[3],q[15];
cx q[3],q[16];
cx q[15],q[20];
rz(4.581677159839479) q[16];
cx q[3],q[16];
cx q[3],q[17];
cx q[16],q[45];
rz(4.581677159839479) q[17];
cx q[3],q[17];
cx q[3],q[18];
rz(4.581677159839479) q[18];
cx q[3],q[18];
cx q[3],q[19];
cx q[4],q[18];
rz(4.581677159839479) q[18];
cx q[4],q[18];
cx q[4],q[21];
rz(4.581677159839479) q[19];
cx q[3],q[19];
cx q[3],q[22];
cx q[7],q[19];
rz(4.581677159839479) q[19];
cx q[7],q[19];
cx q[7],q[60];
cx q[19],q[38];
rz(4.581677159839479) q[20];
cx q[15],q[20];
rz(4.581677159839479) q[21];
cx q[4],q[21];
cx q[4],q[27];
cx q[15],q[21];
rz(4.581677159839479) q[21];
cx q[15],q[21];
cx q[15],q[36];
rz(4.581677159839479) q[22];
cx q[3],q[22];
cx q[3],q[23];
cx q[9],q[22];
rz(4.581677159839479) q[22];
cx q[9],q[22];
cx q[9],q[55];
rx(3.136542363820505) q[22];
rz(4.581677159839479) q[23];
cx q[3],q[23];
cx q[3],q[24];
cx q[17],q[23];
rz(4.581677159839479) q[23];
cx q[17],q[23];
rz(4.581677159839479) q[24];
cx q[3],q[24];
cx q[3],q[25];
cx q[5],q[24];
rz(4.581677159839479) q[24];
cx q[5],q[24];
cx q[5],q[33];
cx q[24],q[54];
rz(4.581677159839479) q[25];
cx q[3],q[25];
cx q[3],q[26];
cx q[12],q[25];
rz(4.581677159839479) q[25];
cx q[12],q[25];
cx q[12],q[31];
rx(3.136542363820505) q[25];
rz(4.581677159839479) q[26];
cx q[3],q[26];
cx q[3],q[28];
cx q[21],q[26];
rz(4.581677159839479) q[26];
cx q[21],q[26];
cx q[21],q[32];
rz(4.581677159839479) q[27];
cx q[4],q[27];
cx q[4],q[47];
cx q[6],q[27];
rz(4.581677159839479) q[27];
cx q[6],q[27];
cx q[6],q[69];
cx q[27],q[41];
rz(4.581677159839479) q[28];
cx q[3],q[28];
cx q[3],q[29];
cx q[28],q[51];
rz(4.581677159839479) q[29];
cx q[3],q[29];
cx q[3],q[30];
rx(3.136542363820505) q[29];
rz(4.581677159839479) q[30];
cx q[3],q[30];
cx q[3],q[34];
cx q[18],q[30];
rz(4.581677159839479) q[30];
cx q[18],q[30];
rx(3.136542363820505) q[18];
rz(4.581677159839479) q[31];
cx q[12],q[31];
cx q[26],q[31];
rz(4.581677159839479) q[31];
cx q[26],q[31];
rx(3.136542363820505) q[26];
rx(3.136542363820505) q[31];
rz(4.581677159839479) q[32];
cx q[21],q[32];
rz(4.581677159839479) q[33];
cx q[5],q[33];
cx q[5],q[46];
cx q[30],q[33];
rz(4.581677159839479) q[33];
cx q[30],q[33];
cx q[30],q[48];
rx(3.136542363820505) q[33];
rz(4.581677159839479) q[34];
cx q[3],q[34];
cx q[3],q[35];
cx q[12],q[34];
rz(4.581677159839479) q[34];
cx q[12],q[34];
cx q[34],q[37];
rz(4.581677159839479) q[35];
cx q[3],q[35];
cx q[3],q[39];
cx q[32],q[35];
rz(4.581677159839479) q[35];
cx q[32],q[35];
rx(3.136542363820505) q[35];
rz(4.581677159839479) q[36];
cx q[15],q[36];
cx q[20],q[36];
rz(4.581677159839479) q[36];
cx q[20],q[36];
rx(3.136542363820505) q[36];
rz(4.581677159839479) q[37];
cx q[34],q[37];
rx(3.136542363820505) q[34];
rx(3.136542363820505) q[37];
rz(4.581677159839479) q[38];
cx q[19],q[38];
rx(3.136542363820505) q[19];
cx q[21],q[38];
rz(4.581677159839479) q[38];
cx q[21],q[38];
rz(4.581677159839479) q[39];
cx q[3],q[39];
cx q[3],q[40];
cx q[13],q[39];
rz(4.581677159839479) q[39];
cx q[13],q[39];
cx q[13],q[56];
rx(3.136542363820505) q[39];
rz(4.581677159839479) q[40];
cx q[3],q[40];
cx q[3],q[42];
cx q[23],q[40];
rz(4.581677159839479) q[40];
cx q[23],q[40];
rx(3.136542363820505) q[40];
rz(4.581677159839479) q[41];
cx q[27],q[41];
cx q[27],q[72];
cx q[41],q[67];
rz(4.581677159839479) q[42];
cx q[3],q[42];
cx q[3],q[43];
cx q[42],q[78];
rz(4.581677159839479) q[43];
cx q[3],q[43];
cx q[3],q[44];
cx q[20],q[43];
rz(4.581677159839479) q[43];
cx q[20],q[43];
rx(3.136542363820505) q[20];
rx(3.136542363820505) q[43];
rz(4.581677159839479) q[44];
cx q[3],q[44];
cx q[3],q[49];
cx q[12],q[44];
rz(4.581677159839479) q[44];
cx q[12],q[44];
rz(4.581677159839479) q[45];
cx q[16],q[45];
cx q[16],q[59];
rz(4.581677159839479) q[46];
cx q[5],q[46];
cx q[5],q[65];
cx q[38],q[46];
rz(4.581677159839479) q[46];
cx q[38],q[46];
rx(3.136542363820505) q[38];
rx(3.136542363820505) q[46];
rz(4.581677159839479) q[47];
cx q[4],q[47];
cx q[17],q[47];
rz(4.581677159839479) q[47];
cx q[17],q[47];
cx q[17],q[53];
rz(4.581677159839479) q[48];
cx q[30],q[48];
rx(3.136542363820505) q[48];
rz(4.581677159839479) q[49];
cx q[3],q[49];
cx q[3],q[50];
cx q[4],q[49];
rz(4.581677159839479) q[49];
cx q[4],q[49];
cx q[4],q[61];
rx(3.136542363820505) q[49];
rz(4.581677159839479) q[50];
cx q[3],q[50];
cx q[3],q[52];
cx q[12],q[50];
rz(4.581677159839479) q[50];
cx q[12],q[50];
cx q[12],q[63];
rz(4.581677159839479) q[51];
cx q[28],q[51];
rx(3.136542363820505) q[51];
rz(4.581677159839479) q[52];
cx q[3],q[52];
cx q[3],q[57];
cx q[10],q[52];
rz(4.581677159839479) q[52];
cx q[10],q[52];
cx q[10],q[64];
rx(3.136542363820505) q[52];
rz(4.581677159839479) q[53];
cx q[17],q[53];
cx q[17],q[62];
cx q[21],q[53];
rz(4.581677159839479) q[53];
cx q[21],q[53];
cx q[21],q[75];
rz(4.581677159839479) q[54];
cx q[24],q[54];
cx q[24],q[58];
cx q[28],q[54];
rz(4.581677159839479) q[54];
cx q[28],q[54];
rx(3.136542363820505) q[54];
rz(4.581677159839479) q[55];
cx q[9],q[55];
cx q[9],q[80];
cx q[15],q[55];
rz(4.581677159839479) q[55];
cx q[15],q[55];
rx(3.136542363820505) q[55];
rz(4.581677159839479) q[56];
cx q[13],q[56];
cx q[45],q[56];
rz(4.581677159839479) q[56];
cx q[45],q[56];
rx(3.136542363820505) q[45];
rz(4.581677159839479) q[57];
cx q[3],q[57];
cx q[3],q[70];
rx(3.136542363820505) q[57];
rz(4.581677159839479) q[58];
cx q[24],q[58];
rx(3.136542363820505) q[24];
cx q[28],q[58];
rz(4.581677159839479) q[58];
cx q[28],q[58];
rx(3.136542363820505) q[28];
rx(3.136542363820505) q[58];
rz(4.581677159839479) q[59];
cx q[16],q[59];
cx q[16],q[73];
cx q[32],q[59];
rz(4.581677159839479) q[59];
cx q[32],q[59];
rz(4.581677159839479) q[60];
cx q[7],q[60];
rz(4.581677159839479) q[61];
cx q[4],q[61];
rx(3.136542363820505) q[4];
cx q[7],q[61];
rz(4.581677159839479) q[61];
cx q[7],q[61];
rx(3.136542363820505) q[7];
rx(3.136542363820505) q[61];
rz(4.581677159839479) q[62];
cx q[17],q[62];
rx(3.136542363820505) q[62];
rz(4.581677159839479) q[63];
cx q[12],q[63];
rx(3.136542363820505) q[12];
cx q[17],q[63];
rz(4.581677159839479) q[63];
cx q[17],q[63];
cx q[17],q[66];
rz(4.581677159839479) q[64];
cx q[10],q[64];
rx(3.136542363820505) q[10];
rx(3.136542363820505) q[64];
rz(4.581677159839479) q[65];
cx q[5],q[65];
cx q[5],q[76];
cx q[23],q[65];
rz(4.581677159839479) q[65];
cx q[23],q[65];
rx(3.136542363820505) q[23];
rx(3.136542363820505) q[65];
rz(4.581677159839479) q[66];
cx q[17],q[66];
rx(3.136542363820505) q[17];
cx q[47],q[66];
rz(4.581677159839479) q[66];
cx q[47],q[66];
rx(3.136542363820505) q[47];
rx(3.136542363820505) q[66];
rz(4.581677159839479) q[67];
cx q[41],q[67];
rx(3.136542363820505) q[41];
cx q[56],q[67];
rz(4.581677159839479) q[67];
cx q[56],q[67];
cx q[56],q[74];
rx(3.136542363820505) q[67];
cx q[68],q[83];
rz(4.581677159839479) q[69];
cx q[6],q[69];
cx q[59],q[69];
rz(4.581677159839479) q[69];
cx q[59],q[69];
rx(3.136542363820505) q[69];
rz(4.581677159839479) q[70];
cx q[3],q[70];
cx q[3],q[71];
cx q[15],q[70];
rz(4.581677159839479) q[70];
cx q[15],q[70];
rx(3.136542363820505) q[70];
rz(4.581677159839479) q[71];
cx q[3],q[71];
cx q[3],q[77];
cx q[53],q[71];
rz(4.581677159839479) q[71];
cx q[53],q[71];
rx(3.136542363820505) q[53];
rx(3.136542363820505) q[71];
rz(4.581677159839479) q[72];
cx q[27],q[72];
rx(3.136542363820505) q[27];
cx q[44],q[72];
rz(4.581677159839479) q[72];
cx q[44],q[72];
rx(3.136542363820505) q[44];
rx(3.136542363820505) q[72];
rz(4.581677159839479) q[73];
cx q[16],q[73];
rx(3.136542363820505) q[16];
cx q[59],q[73];
rz(4.581677159839479) q[73];
cx q[59],q[73];
rx(3.136542363820505) q[59];
rx(3.136542363820505) q[73];
rz(4.581677159839479) q[74];
cx q[56],q[74];
cx q[56],q[82];
cx q[63],q[74];
rz(4.581677159839479) q[74];
cx q[63],q[74];
rx(3.136542363820505) q[63];
rx(3.136542363820505) q[74];
rz(4.581677159839479) q[75];
cx q[21],q[75];
cx q[21],q[81];
rx(3.136542363820505) q[75];
rz(4.581677159839479) q[76];
cx q[5],q[76];
rx(3.136542363820505) q[5];
cx q[6],q[76];
rz(4.581677159839479) q[76];
cx q[6],q[76];
cx q[6],q[79];
rx(3.136542363820505) q[76];
rz(4.581677159839479) q[77];
cx q[3],q[77];
rx(3.136542363820505) q[3];
cx q[0],q[3];
rz(5.439121417687856) q[3];
cx q[0],q[3];
cx q[1],q[3];
rz(5.439121417687856) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(5.439121417687856) q[4];
cx q[1],q[4];
cx q[1],q[5];
cx q[3],q[4];
rz(5.439121417687856) q[4];
cx q[3],q[4];
rz(5.439121417687856) q[5];
cx q[1],q[5];
cx q[3],q[5];
rz(5.439121417687856) q[5];
cx q[3],q[5];
cx q[3],q[7];
rz(5.439121417687856) q[7];
cx q[3],q[7];
cx q[30],q[77];
rz(4.581677159839479) q[77];
cx q[30],q[77];
rx(3.136542363820505) q[30];
rz(4.581677159839479) q[78];
cx q[42],q[78];
rx(3.136542363820505) q[42];
cx q[60],q[78];
rz(4.581677159839479) q[78];
cx q[60],q[78];
rx(3.136542363820505) q[60];
rx(3.136542363820505) q[78];
rz(4.581677159839479) q[79];
cx q[6],q[79];
rx(3.136542363820505) q[6];
cx q[4],q[6];
rz(5.439121417687856) q[6];
cx q[4],q[6];
cx q[4],q[7];
cx q[5],q[6];
rz(5.439121417687856) q[6];
cx q[5],q[6];
rz(5.439121417687856) q[7];
cx q[4],q[7];
cx q[4],q[10];
rz(5.439121417687856) q[10];
cx q[4],q[10];
cx q[6],q[10];
rz(5.439121417687856) q[10];
cx q[6],q[10];
cx q[10],q[37];
rz(5.439121417687856) q[37];
cx q[10],q[37];
cx q[10],q[41];
rz(5.439121417687856) q[41];
cx q[10],q[41];
cx q[50],q[79];
rz(4.581677159839479) q[79];
cx q[50],q[79];
rx(3.136542363820505) q[50];
rx(3.136542363820505) q[79];
rz(4.581677159839479) q[80];
cx q[9],q[80];
rx(3.136542363820505) q[9];
cx q[1],q[9];
rz(5.439121417687856) q[9];
cx q[1],q[9];
cx q[1],q[17];
cx q[15],q[80];
rz(5.439121417687856) q[17];
cx q[1],q[17];
cx q[1],q[28];
rz(5.439121417687856) q[28];
cx q[1],q[28];
cx q[1],q[29];
rz(5.439121417687856) q[29];
cx q[1],q[29];
cx q[1],q[45];
rz(5.439121417687856) q[45];
cx q[1],q[45];
cx q[1],q[57];
rz(5.439121417687856) q[57];
cx q[1],q[57];
cx q[1],q[60];
rz(5.439121417687856) q[60];
cx q[1],q[60];
rx(6.767686082016463) q[1];
rz(4.581677159839479) q[80];
cx q[15],q[80];
rx(3.136542363820505) q[15];
cx q[0],q[15];
rz(5.439121417687856) q[15];
cx q[0],q[15];
cx q[0],q[16];
rz(5.439121417687856) q[16];
cx q[0],q[16];
cx q[0],q[20];
rz(5.439121417687856) q[20];
cx q[0],q[20];
rx(3.136542363820505) q[80];
rz(4.581677159839479) q[81];
cx q[21],q[81];
rx(3.136542363820505) q[21];
cx q[77],q[81];
rz(4.581677159839479) q[81];
cx q[77],q[81];
rx(3.136542363820505) q[77];
rx(3.136542363820505) q[81];
rz(4.581677159839479) q[82];
cx q[56],q[82];
rx(3.136542363820505) q[56];
rx(3.136542363820505) q[82];
rz(0.42920412547152276) q[83];
cx q[68],q[83];
rx(9.517239446365442) q[68];
cx q[13],q[68];
rz(4.581677159839479) q[68];
cx q[13],q[68];
rx(3.136542363820505) q[13];
cx q[4],q[13];
rz(5.439121417687856) q[13];
cx q[4],q[13];
cx q[32],q[68];
rz(4.581677159839479) q[68];
cx q[32],q[68];
rx(3.136542363820505) q[32];
cx q[0],q[32];
rz(5.439121417687856) q[32];
cx q[0],q[32];
cx q[0],q[42];
rz(5.439121417687856) q[42];
cx q[0],q[42];
cx q[0],q[48];
rz(5.439121417687856) q[48];
cx q[0],q[48];
cx q[0],q[51];
rz(5.439121417687856) q[51];
cx q[0],q[51];
cx q[0],q[62];
rz(5.439121417687856) q[62];
cx q[0],q[62];
cx q[0],q[64];
rz(5.439121417687856) q[64];
cx q[0],q[64];
cx q[0],q[75];
rz(5.439121417687856) q[75];
cx q[0],q[75];
cx q[0],q[82];
rz(5.439121417687856) q[82];
cx q[0],q[82];
rx(6.767686082016463) q[0];
rx(9.517239446365442) q[83];
cx q[8],q[83];
rz(4.581677159839479) q[83];
cx q[8],q[83];
rx(3.136542363820505) q[8];
cx q[3],q[8];
rz(5.439121417687856) q[8];
cx q[3],q[8];
cx q[3],q[9];
cx q[5],q[8];
rz(5.439121417687856) q[8];
cx q[5],q[8];
cx q[5],q[11];
rz(5.439121417687856) q[9];
cx q[3],q[9];
cx q[3],q[12];
rz(5.439121417687856) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(5.439121417687856) q[11];
cx q[6],q[11];
rx(6.767686082016463) q[11];
rz(5.439121417687856) q[12];
cx q[3],q[12];
cx q[3],q[14];
cx q[5],q[12];
rz(5.439121417687856) q[12];
cx q[5],q[12];
cx q[5],q[13];
rz(5.439121417687856) q[13];
cx q[5],q[13];
rz(5.439121417687856) q[14];
cx q[3],q[14];
cx q[3],q[15];
cx q[4],q[14];
rz(5.439121417687856) q[14];
cx q[4],q[14];
rx(6.767686082016463) q[14];
rz(5.439121417687856) q[15];
cx q[3],q[15];
cx q[3],q[16];
cx q[15],q[20];
rz(5.439121417687856) q[16];
cx q[3],q[16];
cx q[3],q[17];
cx q[16],q[45];
rz(5.439121417687856) q[17];
cx q[3],q[17];
cx q[3],q[18];
rz(5.439121417687856) q[18];
cx q[3],q[18];
cx q[3],q[19];
cx q[4],q[18];
rz(5.439121417687856) q[18];
cx q[4],q[18];
cx q[4],q[21];
rz(5.439121417687856) q[19];
cx q[3],q[19];
cx q[3],q[22];
cx q[7],q[19];
rz(5.439121417687856) q[19];
cx q[7],q[19];
cx q[7],q[60];
cx q[19],q[38];
rz(5.439121417687856) q[20];
cx q[15],q[20];
rz(5.439121417687856) q[21];
cx q[4],q[21];
cx q[4],q[27];
cx q[15],q[21];
rz(5.439121417687856) q[21];
cx q[15],q[21];
cx q[15],q[36];
rz(5.439121417687856) q[22];
cx q[3],q[22];
cx q[3],q[23];
cx q[9],q[22];
rz(5.439121417687856) q[22];
cx q[9],q[22];
cx q[9],q[55];
rx(6.767686082016463) q[22];
rz(5.439121417687856) q[23];
cx q[3],q[23];
cx q[3],q[24];
cx q[17],q[23];
rz(5.439121417687856) q[23];
cx q[17],q[23];
rz(5.439121417687856) q[24];
cx q[3],q[24];
cx q[3],q[25];
cx q[5],q[24];
rz(5.439121417687856) q[24];
cx q[5],q[24];
cx q[5],q[33];
cx q[24],q[54];
rz(5.439121417687856) q[25];
cx q[3],q[25];
cx q[3],q[26];
cx q[12],q[25];
rz(5.439121417687856) q[25];
cx q[12],q[25];
cx q[12],q[31];
rx(6.767686082016463) q[25];
rz(5.439121417687856) q[26];
cx q[3],q[26];
cx q[3],q[28];
cx q[21],q[26];
rz(5.439121417687856) q[26];
cx q[21],q[26];
cx q[21],q[32];
rz(5.439121417687856) q[27];
cx q[4],q[27];
cx q[4],q[47];
cx q[6],q[27];
rz(5.439121417687856) q[27];
cx q[6],q[27];
cx q[6],q[69];
cx q[27],q[41];
rz(5.439121417687856) q[28];
cx q[3],q[28];
cx q[3],q[29];
cx q[28],q[51];
rz(5.439121417687856) q[29];
cx q[3],q[29];
cx q[3],q[30];
rx(6.767686082016463) q[29];
rz(5.439121417687856) q[30];
cx q[3],q[30];
cx q[3],q[34];
cx q[18],q[30];
rz(5.439121417687856) q[30];
cx q[18],q[30];
rx(6.767686082016463) q[18];
rz(5.439121417687856) q[31];
cx q[12],q[31];
cx q[26],q[31];
rz(5.439121417687856) q[31];
cx q[26],q[31];
rx(6.767686082016463) q[26];
rx(6.767686082016463) q[31];
rz(5.439121417687856) q[32];
cx q[21],q[32];
rz(5.439121417687856) q[33];
cx q[5],q[33];
cx q[5],q[46];
cx q[30],q[33];
rz(5.439121417687856) q[33];
cx q[30],q[33];
cx q[30],q[48];
rx(6.767686082016463) q[33];
rz(5.439121417687856) q[34];
cx q[3],q[34];
cx q[3],q[35];
cx q[12],q[34];
rz(5.439121417687856) q[34];
cx q[12],q[34];
cx q[34],q[37];
rz(5.439121417687856) q[35];
cx q[3],q[35];
cx q[3],q[39];
cx q[32],q[35];
rz(5.439121417687856) q[35];
cx q[32],q[35];
rx(6.767686082016463) q[35];
rz(5.439121417687856) q[36];
cx q[15],q[36];
cx q[20],q[36];
rz(5.439121417687856) q[36];
cx q[20],q[36];
rx(6.767686082016463) q[36];
rz(5.439121417687856) q[37];
cx q[34],q[37];
rx(6.767686082016463) q[34];
rx(6.767686082016463) q[37];
rz(5.439121417687856) q[38];
cx q[19],q[38];
rx(6.767686082016463) q[19];
cx q[21],q[38];
rz(5.439121417687856) q[38];
cx q[21],q[38];
rz(5.439121417687856) q[39];
cx q[3],q[39];
cx q[3],q[40];
cx q[13],q[39];
rz(5.439121417687856) q[39];
cx q[13],q[39];
cx q[13],q[56];
rx(6.767686082016463) q[39];
rz(5.439121417687856) q[40];
cx q[3],q[40];
cx q[3],q[42];
cx q[23],q[40];
rz(5.439121417687856) q[40];
cx q[23],q[40];
rx(6.767686082016463) q[40];
rz(5.439121417687856) q[41];
cx q[27],q[41];
cx q[27],q[72];
cx q[41],q[67];
rz(5.439121417687856) q[42];
cx q[3],q[42];
cx q[3],q[43];
cx q[42],q[78];
rz(5.439121417687856) q[43];
cx q[3],q[43];
cx q[3],q[44];
cx q[20],q[43];
rz(5.439121417687856) q[43];
cx q[20],q[43];
rx(6.767686082016463) q[20];
rx(6.767686082016463) q[43];
rz(5.439121417687856) q[44];
cx q[3],q[44];
cx q[3],q[49];
cx q[12],q[44];
rz(5.439121417687856) q[44];
cx q[12],q[44];
rz(5.439121417687856) q[45];
cx q[16],q[45];
cx q[16],q[59];
rz(5.439121417687856) q[46];
cx q[5],q[46];
cx q[5],q[65];
cx q[38],q[46];
rz(5.439121417687856) q[46];
cx q[38],q[46];
rx(6.767686082016463) q[38];
rx(6.767686082016463) q[46];
rz(5.439121417687856) q[47];
cx q[4],q[47];
cx q[17],q[47];
rz(5.439121417687856) q[47];
cx q[17],q[47];
cx q[17],q[53];
rz(5.439121417687856) q[48];
cx q[30],q[48];
rx(6.767686082016463) q[48];
rz(5.439121417687856) q[49];
cx q[3],q[49];
cx q[3],q[50];
cx q[4],q[49];
rz(5.439121417687856) q[49];
cx q[4],q[49];
cx q[4],q[61];
rx(6.767686082016463) q[49];
rz(5.439121417687856) q[50];
cx q[3],q[50];
cx q[3],q[52];
cx q[12],q[50];
rz(5.439121417687856) q[50];
cx q[12],q[50];
cx q[12],q[63];
rz(5.439121417687856) q[51];
cx q[28],q[51];
rx(6.767686082016463) q[51];
rz(5.439121417687856) q[52];
cx q[3],q[52];
cx q[3],q[57];
cx q[10],q[52];
rz(5.439121417687856) q[52];
cx q[10],q[52];
cx q[10],q[64];
rx(6.767686082016463) q[52];
rz(5.439121417687856) q[53];
cx q[17],q[53];
cx q[17],q[62];
cx q[21],q[53];
rz(5.439121417687856) q[53];
cx q[21],q[53];
cx q[21],q[75];
rz(5.439121417687856) q[54];
cx q[24],q[54];
cx q[24],q[58];
cx q[28],q[54];
rz(5.439121417687856) q[54];
cx q[28],q[54];
rx(6.767686082016463) q[54];
rz(5.439121417687856) q[55];
cx q[9],q[55];
cx q[9],q[80];
cx q[15],q[55];
rz(5.439121417687856) q[55];
cx q[15],q[55];
rx(6.767686082016463) q[55];
rz(5.439121417687856) q[56];
cx q[13],q[56];
cx q[45],q[56];
rz(5.439121417687856) q[56];
cx q[45],q[56];
rx(6.767686082016463) q[45];
rz(5.439121417687856) q[57];
cx q[3],q[57];
cx q[3],q[70];
rx(6.767686082016463) q[57];
rz(5.439121417687856) q[58];
cx q[24],q[58];
rx(6.767686082016463) q[24];
cx q[28],q[58];
rz(5.439121417687856) q[58];
cx q[28],q[58];
rx(6.767686082016463) q[28];
rx(6.767686082016463) q[58];
rz(5.439121417687856) q[59];
cx q[16],q[59];
cx q[16],q[73];
cx q[32],q[59];
rz(5.439121417687856) q[59];
cx q[32],q[59];
rz(5.439121417687856) q[60];
cx q[7],q[60];
rz(5.439121417687856) q[61];
cx q[4],q[61];
rx(6.767686082016463) q[4];
cx q[7],q[61];
rz(5.439121417687856) q[61];
cx q[7],q[61];
rx(6.767686082016463) q[7];
rx(6.767686082016463) q[61];
rz(5.439121417687856) q[62];
cx q[17],q[62];
rx(6.767686082016463) q[62];
rz(5.439121417687856) q[63];
cx q[12],q[63];
rx(6.767686082016463) q[12];
cx q[17],q[63];
rz(5.439121417687856) q[63];
cx q[17],q[63];
cx q[17],q[66];
rz(5.439121417687856) q[64];
cx q[10],q[64];
rx(6.767686082016463) q[10];
rx(6.767686082016463) q[64];
rz(5.439121417687856) q[65];
cx q[5],q[65];
cx q[5],q[76];
cx q[23],q[65];
rz(5.439121417687856) q[65];
cx q[23],q[65];
rx(6.767686082016463) q[23];
rx(6.767686082016463) q[65];
rz(5.439121417687856) q[66];
cx q[17],q[66];
rx(6.767686082016463) q[17];
cx q[47],q[66];
rz(5.439121417687856) q[66];
cx q[47],q[66];
rx(6.767686082016463) q[47];
rx(6.767686082016463) q[66];
rz(5.439121417687856) q[67];
cx q[41],q[67];
rx(6.767686082016463) q[41];
cx q[56],q[67];
rz(5.439121417687856) q[67];
cx q[56],q[67];
cx q[56],q[74];
rx(6.767686082016463) q[67];
cx q[68],q[83];
rz(5.439121417687856) q[69];
cx q[6],q[69];
cx q[59],q[69];
rz(5.439121417687856) q[69];
cx q[59],q[69];
rx(6.767686082016463) q[69];
rz(5.439121417687856) q[70];
cx q[3],q[70];
cx q[3],q[71];
cx q[15],q[70];
rz(5.439121417687856) q[70];
cx q[15],q[70];
rx(6.767686082016463) q[70];
rz(5.439121417687856) q[71];
cx q[3],q[71];
cx q[3],q[77];
cx q[53],q[71];
rz(5.439121417687856) q[71];
cx q[53],q[71];
rx(6.767686082016463) q[53];
rx(6.767686082016463) q[71];
rz(5.439121417687856) q[72];
cx q[27],q[72];
rx(6.767686082016463) q[27];
cx q[44],q[72];
rz(5.439121417687856) q[72];
cx q[44],q[72];
rx(6.767686082016463) q[44];
rx(6.767686082016463) q[72];
rz(5.439121417687856) q[73];
cx q[16],q[73];
rx(6.767686082016463) q[16];
cx q[59],q[73];
rz(5.439121417687856) q[73];
cx q[59],q[73];
rx(6.767686082016463) q[59];
rx(6.767686082016463) q[73];
rz(5.439121417687856) q[74];
cx q[56],q[74];
cx q[56],q[82];
cx q[63],q[74];
rz(5.439121417687856) q[74];
cx q[63],q[74];
rx(6.767686082016463) q[63];
rx(6.767686082016463) q[74];
rz(5.439121417687856) q[75];
cx q[21],q[75];
cx q[21],q[81];
rx(6.767686082016463) q[75];
rz(5.439121417687856) q[76];
cx q[5],q[76];
rx(6.767686082016463) q[5];
cx q[6],q[76];
rz(5.439121417687856) q[76];
cx q[6],q[76];
cx q[6],q[79];
rx(6.767686082016463) q[76];
rz(5.439121417687856) q[77];
cx q[3],q[77];
rx(6.767686082016463) q[3];
cx q[30],q[77];
rz(5.439121417687856) q[77];
cx q[30],q[77];
rx(6.767686082016463) q[30];
rz(5.439121417687856) q[78];
cx q[42],q[78];
rx(6.767686082016463) q[42];
cx q[60],q[78];
rz(5.439121417687856) q[78];
cx q[60],q[78];
rx(6.767686082016463) q[60];
rx(6.767686082016463) q[78];
rz(5.439121417687856) q[79];
cx q[6],q[79];
rx(6.767686082016463) q[6];
cx q[50],q[79];
rz(5.439121417687856) q[79];
cx q[50],q[79];
rx(6.767686082016463) q[50];
rx(6.767686082016463) q[79];
rz(5.439121417687856) q[80];
cx q[9],q[80];
rx(6.767686082016463) q[9];
cx q[15],q[80];
rz(5.439121417687856) q[80];
cx q[15],q[80];
rx(6.767686082016463) q[15];
rx(6.767686082016463) q[80];
rz(5.439121417687856) q[81];
cx q[21],q[81];
rx(6.767686082016463) q[21];
cx q[77],q[81];
rz(5.439121417687856) q[81];
cx q[77],q[81];
rx(6.767686082016463) q[77];
rx(6.767686082016463) q[81];
rz(5.439121417687856) q[82];
cx q[56],q[82];
rx(6.767686082016463) q[56];
rx(6.767686082016463) q[82];
rz(4.581677159839479) q[83];
cx q[68],q[83];
rx(3.136542363820505) q[68];
cx q[13],q[68];
rz(5.439121417687856) q[68];
cx q[13],q[68];
rx(6.767686082016463) q[13];
cx q[32],q[68];
rz(5.439121417687856) q[68];
cx q[32],q[68];
rx(6.767686082016463) q[32];
rx(3.136542363820505) q[83];
cx q[8],q[83];
rz(5.439121417687856) q[83];
cx q[8],q[83];
rx(6.767686082016463) q[8];
cx q[68],q[83];
rz(5.439121417687856) q[83];
cx q[68],q[83];
rx(6.767686082016463) q[68];
rx(6.767686082016463) q[83];