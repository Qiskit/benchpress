OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
ry(pi/2) q[0];
rx(pi) q[0];
ry(pi/2) q[1];
rx(pi) q[1];
cx q[0],q[1];
rz(4.087814441999027) q[1];
cx q[0],q[1];
ry(pi/2) q[2];
rx(pi) q[2];
cx q[0],q[2];
rz(4.087814441999027) q[2];
cx q[0],q[2];
rx(8.130584046955743) q[2];
ry(pi/2) q[3];
rx(pi) q[3];
cx q[0],q[3];
rz(4.087814441999027) q[3];
cx q[0],q[3];
rx(8.130584046955743) q[0];
cx q[1],q[3];
rz(4.087814441999027) q[3];
cx q[1],q[3];
ry(pi/2) q[4];
rx(pi) q[4];
cx q[1],q[4];
rz(4.087814441999027) q[4];
cx q[1],q[4];
cx q[3],q[4];
rz(4.087814441999027) q[4];
cx q[3],q[4];
rx(8.130584046955743) q[4];
ry(pi/2) q[5];
rx(pi) q[5];
cx q[1],q[5];
rz(4.087814441999027) q[5];
cx q[1],q[5];
rx(8.130584046955743) q[1];
cx q[0],q[1];
rz(5.367315223278074) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(5.367315223278074) q[2];
cx q[0],q[2];
rx(7.493346448775371) q[2];
cx q[3],q[5];
rz(4.087814441999027) q[5];
cx q[3],q[5];
rx(8.130584046955743) q[3];
cx q[0],q[3];
rz(5.367315223278074) q[3];
cx q[0],q[3];
rx(7.493346448775371) q[0];
cx q[1],q[3];
rz(5.367315223278074) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(5.367315223278074) q[4];
cx q[1],q[4];
cx q[3],q[4];
rz(5.367315223278074) q[4];
cx q[3],q[4];
rx(7.493346448775371) q[4];
rx(8.130584046955743) q[5];
cx q[1],q[5];
rz(5.367315223278074) q[5];
cx q[1],q[5];
rx(7.493346448775371) q[1];
cx q[0],q[1];
rz(1.782725198170932) q[1];
cx q[0],q[1];
cx q[0],q[2];
rz(1.782725198170932) q[2];
cx q[0],q[2];
rx(12.118770308851422) q[2];
cx q[3],q[5];
rz(5.367315223278074) q[5];
cx q[3],q[5];
rx(7.493346448775371) q[3];
cx q[0],q[3];
rz(1.782725198170932) q[3];
cx q[0],q[3];
rx(12.118770308851422) q[0];
cx q[1],q[3];
rz(1.782725198170932) q[3];
cx q[1],q[3];
cx q[1],q[4];
rz(1.782725198170932) q[4];
cx q[1],q[4];
cx q[3],q[4];
rz(1.782725198170932) q[4];
cx q[3],q[4];
rx(12.118770308851422) q[4];
rx(7.493346448775371) q[5];
cx q[1],q[5];
rz(1.782725198170932) q[5];
cx q[1],q[5];
rx(12.118770308851422) q[1];
cx q[3],q[5];
rz(1.782725198170932) q[5];
cx q[3],q[5];
rx(12.118770308851422) q[3];
rx(12.118770308851422) q[5];