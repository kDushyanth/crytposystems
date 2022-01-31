# crytposystems
RSA and ElGamal implementation using [Charm-Crypto](https://jhuisi.github.io/charm/)
* RSA Cryptosystem (Based on Factorization Problem)
1.   Select large primes p, q such that p≠ q
2.   Calculate n = p*q and Ø(n) = (p-1)*(q-1)
3.   Select `b` such that gcd(Ø(n),b) = 1 and 1<b< Ø(n)
4.   Compute `d` such that bd ≅ 1(mod Ø(n))
5.   Public key (n, b) and private key (d,n)
6.   Encryption for message `m`: c = E<sub>k</sub>(m) = m<sup>b</sup>(mod n)
7.   Decryption for cipher `c`: D<sub>k</sub>(c) = c<sup>d</sup>(mod n)

* ElGamal Cryptosystem (Based on Discrete Logarithm)
1.   p: Prime, (Z<sub>p</sub><sup>\*</sup>, . ) and α ∈ Z<sub>p</sub><sup>\*</sup> primitive element.
2.   {(p, α, a, ß): α<sup>a</sup> ≅ ß (mod p)}
3.   Public Key: (p, α, ß) and Private Key: a
4.   Encryption for message `m`: Select random number r ∈ Z<sub>p-1</sub><sup>\*</sup>  
       c = E<sub>k</sub>(m) = (y<sub>1</sub>,y<sub>2</sub>) where y<sub>1</sub> = α<sup>r</sup> (mod p) and y<sub>2</sub> = m. ß<sup>r</sup>(mod p)
5.   Decryption for cipher `c`: D<sub>k</sub>(c) = y<sub>2</sub>.(y<sub>1</sub><sup>a</sup>)<sup>-1</sup>
