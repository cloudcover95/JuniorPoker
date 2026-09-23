// Drop-in muck trough. Poker card ~63.5 x 88.9 mm. OpenSCAD.
card_w = 63.5;
card_h = 88.9;
wall = 2.4;
n = 80;
// stack height rough 0.3mm * n
H = 0.3 * n + 12;
W = card_w + 8;
D = card_h + 10;
difference() {
  cube([W + 2*wall, D + 2*wall, H]);
  translate([wall, wall, wall]) cube([W, D, H]);
}
