OPENQASM 2.0;
include "qelib1.inc";
qreg q[21];
ry(pi/2) q[0];
rx(pi) q[0];
ry(pi/2) q[1];
rx(pi) q[1];
cx q[0],q[1];
rz(4.902053087356601) q[1];
cx q[0],q[1];
ry(pi/2) q[2];
rx(pi) q[2];
cx q[0],q[2];
rz(4.902053087356601) q[2];
cx q[0],q[2];
rx(11.53630276043216) q[2];
ry(pi/2) q[3];
rx(pi) q[3];
cx q[0],q[3];
rz(4.902053087356601) q[3];
cx q[0],q[3];
cx q[1],q[3];
rz(4.902053087356601) q[3];
cx q[1],q[3];
ry(pi/2) q[4];
rx(pi) q[4];
cx q[1],q[4];
rz(4.902053087356601) q[4];
cx q[1],q[4];
cx q[3],q[4];
rz(4.902053087356601) q[4];
cx q[3],q[4];
ry(pi/2) q[5];
rx(pi) q[5];
cx q[1],q[5];
rz(4.902053087356601) q[5];
cx q[1],q[5];
cx q[3],q[5];
rz(4.902053087356601) q[5];
cx q[3],q[5];
ry(pi/2) q[6];
rx(pi) q[6];
cx q[4],q[6];
rz(4.902053087356601) q[6];
cx q[4],q[6];
cx q[5],q[6];
rz(4.902053087356601) q[6];
cx q[5],q[6];
ry(pi/2) q[7];
rx(pi) q[7];
cx q[3],q[7];
rz(4.902053087356601) q[7];
cx q[3],q[7];
cx q[4],q[7];
rz(4.902053087356601) q[7];
cx q[4],q[7];
ry(pi/2) q[8];
rx(pi) q[8];
cx q[3],q[8];
rz(4.902053087356601) q[8];
cx q[3],q[8];
cx q[5],q[8];
rz(4.902053087356601) q[8];
cx q[5],q[8];
rx(11.53630276043216) q[8];
ry(pi/2) q[9];
rx(pi) q[9];
cx q[1],q[9];
rz(4.902053087356601) q[9];
cx q[1],q[9];
cx q[3],q[9];
rz(4.902053087356601) q[9];
cx q[3],q[9];
rx(11.53630276043216) q[9];
ry(pi/2) q[10];
rx(pi) q[10];
cx q[4],q[10];
rz(4.902053087356601) q[10];
cx q[4],q[10];
cx q[6],q[10];
rz(4.902053087356601) q[10];
cx q[6],q[10];
rx(11.53630276043216) q[10];
ry(pi/2) q[11];
rx(pi) q[11];
cx q[5],q[11];
rz(4.902053087356601) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(4.902053087356601) q[11];
cx q[6],q[11];
rx(11.53630276043216) q[6];
rx(11.53630276043216) q[11];
ry(pi/2) q[12];
rx(pi) q[12];
cx q[3],q[12];
rz(4.902053087356601) q[12];
cx q[3],q[12];
cx q[5],q[12];
rz(4.902053087356601) q[12];
cx q[5],q[12];
rx(11.53630276043216) q[12];
ry(pi/2) q[13];
rx(pi) q[13];
cx q[4],q[13];
rz(4.902053087356601) q[13];
cx q[4],q[13];
cx q[5],q[13];
rz(4.902053087356601) q[13];
cx q[5],q[13];
rx(11.53630276043216) q[5];
rx(11.53630276043216) q[13];
ry(pi/2) q[14];
rx(pi) q[14];
cx q[3],q[14];
rz(4.902053087356601) q[14];
cx q[3],q[14];
cx q[4],q[14];
rz(4.902053087356601) q[14];
cx q[4],q[14];
rx(11.53630276043216) q[14];
ry(pi/2) q[15];
rx(pi) q[15];
cx q[0],q[15];
rz(4.902053087356601) q[15];
cx q[0],q[15];
cx q[3],q[15];
rz(4.902053087356601) q[15];
cx q[3],q[15];
ry(pi/2) q[16];
rx(pi) q[16];
cx q[0],q[16];
rz(4.902053087356601) q[16];
cx q[0],q[16];
cx q[3],q[16];
rz(4.902053087356601) q[16];
cx q[3],q[16];
rx(11.53630276043216) q[16];
ry(pi/2) q[17];
rx(pi) q[17];
cx q[1],q[17];
rz(4.902053087356601) q[17];
cx q[1],q[17];
rx(11.53630276043216) q[1];
cx q[3],q[17];
rz(4.902053087356601) q[17];
cx q[3],q[17];
rx(11.53630276043216) q[17];
ry(pi/2) q[18];
rx(pi) q[18];
cx q[3],q[18];
rz(4.902053087356601) q[18];
cx q[3],q[18];
cx q[4],q[18];
rz(4.902053087356601) q[18];
cx q[4],q[18];
rx(11.53630276043216) q[4];
rx(11.53630276043216) q[18];
ry(pi/2) q[19];
rx(pi) q[19];
cx q[3],q[19];
rz(4.902053087356601) q[19];
cx q[3],q[19];
rx(11.53630276043216) q[3];
cx q[7],q[19];
rz(4.902053087356601) q[19];
cx q[7],q[19];
rx(11.53630276043216) q[7];
rx(11.53630276043216) q[19];
ry(pi/2) q[20];
rx(pi) q[20];
cx q[0],q[20];
rz(4.902053087356601) q[20];
cx q[0],q[20];
rx(11.53630276043216) q[0];
cx q[0],q[1];
rz(4.748351113212669) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(4.748351113212669) q[2];
cx q[0],q[2];
cx q[0],q[3];
rx(10.590529641921101) q[2];
rz(4.748351113212669) q[3];
cx q[0],q[3];
cx q[1],q[3];
rz(4.748351113212669) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(4.748351113212669) q[4];
cx q[1],q[4];
cx q[1],q[5];
cx q[3],q[4];
rz(4.748351113212669) q[4];
cx q[3],q[4];
cx q[4],q[6];
rz(4.748351113212669) q[5];
cx q[1],q[5];
cx q[1],q[9];
cx q[3],q[5];
rz(4.748351113212669) q[5];
cx q[3],q[5];
cx q[3],q[7];
rz(4.748351113212669) q[6];
cx q[4],q[6];
cx q[5],q[6];
rz(4.748351113212669) q[6];
cx q[5],q[6];
rz(4.748351113212669) q[7];
cx q[3],q[7];
cx q[3],q[8];
cx q[4],q[7];
rz(4.748351113212669) q[7];
cx q[4],q[7];
cx q[4],q[10];
rz(4.748351113212669) q[8];
cx q[3],q[8];
cx q[5],q[8];
rz(4.748351113212669) q[8];
cx q[5],q[8];
cx q[5],q[11];
rx(10.590529641921101) q[8];
rz(4.748351113212669) q[9];
cx q[1],q[9];
cx q[1],q[17];
cx q[3],q[9];
rz(4.748351113212669) q[9];
cx q[3],q[9];
cx q[3],q[12];
rx(10.590529641921101) q[9];
rz(4.748351113212669) q[10];
cx q[4],q[10];
cx q[4],q[13];
cx q[6],q[10];
rz(4.748351113212669) q[10];
cx q[6],q[10];
rx(10.590529641921101) q[10];
rz(4.748351113212669) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(4.748351113212669) q[11];
cx q[6],q[11];
rx(10.590529641921101) q[6];
rx(10.590529641921101) q[11];
rz(4.748351113212669) q[12];
cx q[3],q[12];
cx q[3],q[14];
cx q[5],q[12];
rz(4.748351113212669) q[12];
cx q[5],q[12];
rx(10.590529641921101) q[12];
rz(4.748351113212669) q[13];
cx q[4],q[13];
cx q[5],q[13];
rz(4.748351113212669) q[13];
cx q[5],q[13];
rx(10.590529641921101) q[5];
rx(10.590529641921101) q[13];
rz(4.748351113212669) q[14];
cx q[3],q[14];
cx q[4],q[14];
rz(4.748351113212669) q[14];
cx q[4],q[14];
rx(10.590529641921101) q[14];
cx q[15],q[20];
rz(4.748351113212669) q[17];
cx q[1],q[17];
rx(10.590529641921101) q[1];
rz(4.902053087356601) q[20];
cx q[15],q[20];
rx(11.53630276043216) q[15];
cx q[0],q[15];
rz(4.748351113212669) q[15];
cx q[0],q[15];
cx q[0],q[16];
cx q[3],q[15];
rz(4.748351113212669) q[15];
cx q[3],q[15];
rz(4.748351113212669) q[16];
cx q[0],q[16];
cx q[3],q[16];
rz(4.748351113212669) q[16];
cx q[3],q[16];
cx q[3],q[17];
rx(10.590529641921101) q[16];
rz(4.748351113212669) q[17];
cx q[3],q[17];
cx q[3],q[18];
rx(10.590529641921101) q[17];
rz(4.748351113212669) q[18];
cx q[3],q[18];
cx q[3],q[19];
cx q[4],q[18];
rz(4.748351113212669) q[18];
cx q[4],q[18];
rx(10.590529641921101) q[4];
rx(10.590529641921101) q[18];
rz(4.748351113212669) q[19];
cx q[3],q[19];
rx(10.590529641921101) q[3];
cx q[7],q[19];
rz(4.748351113212669) q[19];
cx q[7],q[19];
rx(10.590529641921101) q[7];
rx(10.590529641921101) q[19];
rx(11.53630276043216) q[20];
cx q[0],q[20];
rz(4.748351113212669) q[20];
cx q[0],q[20];
rx(10.590529641921101) q[0];
cx q[0],q[1];
rz(3.474473616362654) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(3.474473616362654) q[2];
cx q[0],q[2];
cx q[0],q[3];
rx(3.7913507840644223) q[2];
rz(3.474473616362654) q[3];
cx q[0],q[3];
cx q[1],q[3];
rz(3.474473616362654) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(3.474473616362654) q[4];
cx q[1],q[4];
cx q[1],q[5];
cx q[3],q[4];
rz(3.474473616362654) q[4];
cx q[3],q[4];
cx q[4],q[6];
rz(3.474473616362654) q[5];
cx q[1],q[5];
cx q[1],q[9];
cx q[3],q[5];
rz(3.474473616362654) q[5];
cx q[3],q[5];
cx q[3],q[7];
rz(3.474473616362654) q[6];
cx q[4],q[6];
cx q[5],q[6];
rz(3.474473616362654) q[6];
cx q[5],q[6];
rz(3.474473616362654) q[7];
cx q[3],q[7];
cx q[3],q[8];
cx q[4],q[7];
rz(3.474473616362654) q[7];
cx q[4],q[7];
cx q[4],q[10];
rz(3.474473616362654) q[8];
cx q[3],q[8];
cx q[5],q[8];
rz(3.474473616362654) q[8];
cx q[5],q[8];
cx q[5],q[11];
rx(3.7913507840644223) q[8];
rz(3.474473616362654) q[9];
cx q[1],q[9];
cx q[1],q[17];
cx q[3],q[9];
rz(3.474473616362654) q[9];
cx q[3],q[9];
cx q[3],q[12];
rx(3.7913507840644223) q[9];
rz(3.474473616362654) q[10];
cx q[4],q[10];
cx q[4],q[13];
cx q[6],q[10];
rz(3.474473616362654) q[10];
cx q[6],q[10];
rx(3.7913507840644223) q[10];
rz(3.474473616362654) q[11];
cx q[5],q[11];
cx q[6],q[11];
rz(3.474473616362654) q[11];
cx q[6],q[11];
rx(3.7913507840644223) q[6];
rx(3.7913507840644223) q[11];
rz(3.474473616362654) q[12];
cx q[3],q[12];
cx q[3],q[14];
cx q[5],q[12];
rz(3.474473616362654) q[12];
cx q[5],q[12];
rx(3.7913507840644223) q[12];
rz(3.474473616362654) q[13];
cx q[4],q[13];
cx q[5],q[13];
rz(3.474473616362654) q[13];
cx q[5],q[13];
rx(3.7913507840644223) q[5];
rx(3.7913507840644223) q[13];
rz(3.474473616362654) q[14];
cx q[3],q[14];
cx q[4],q[14];
rz(3.474473616362654) q[14];
cx q[4],q[14];
rx(3.7913507840644223) q[14];
cx q[15],q[20];
rz(3.474473616362654) q[17];
cx q[1],q[17];
rx(3.7913507840644223) q[1];
rz(4.748351113212669) q[20];
cx q[15],q[20];
rx(10.590529641921101) q[15];
cx q[0],q[15];
rz(3.474473616362654) q[15];
cx q[0],q[15];
cx q[0],q[16];
cx q[3],q[15];
rz(3.474473616362654) q[15];
cx q[3],q[15];
rz(3.474473616362654) q[16];
cx q[0],q[16];
cx q[3],q[16];
rz(3.474473616362654) q[16];
cx q[3],q[16];
cx q[3],q[17];
rx(3.7913507840644223) q[16];
rz(3.474473616362654) q[17];
cx q[3],q[17];
cx q[3],q[18];
rx(3.7913507840644223) q[17];
rz(3.474473616362654) q[18];
cx q[3],q[18];
cx q[3],q[19];
cx q[4],q[18];
rz(3.474473616362654) q[18];
cx q[4],q[18];
rx(3.7913507840644223) q[4];
rx(3.7913507840644223) q[18];
rz(3.474473616362654) q[19];
cx q[3],q[19];
rx(3.7913507840644223) q[3];
cx q[7],q[19];
rz(3.474473616362654) q[19];
cx q[7],q[19];
rx(3.7913507840644223) q[7];
rx(3.7913507840644223) q[19];
rx(10.590529641921101) q[20];
cx q[0],q[20];
rz(3.474473616362654) q[20];
cx q[0],q[20];
rx(3.7913507840644223) q[0];
cx q[15],q[20];
rz(3.474473616362654) q[20];
cx q[15],q[20];
rx(3.7913507840644223) q[15];
rx(3.7913507840644223) q[20];