from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from Crypto.Util.number import getPrime
from gmpy2 import invert
p = 11676051195515049069996596285348749900918078079741419763055417273203101611022118459167938039506145514281756244210361136569542410
q = 10315984123984774457662212691496628969472212373691807981769204403439398786435378656107178613432673000807327132053727674042100214
e = 65537
c = 20343085339425793640864363014691172523335794854995674420425397084628460201685540859699058586640215807169674729533033759504677263
# decrypt
n = p*q
phi_n = (p-1)*(q-1)
d = inverse(e, phi_n) # or d = invert(e, phin)
m = pow(c, d, n)
print(long_to_bytes(m))