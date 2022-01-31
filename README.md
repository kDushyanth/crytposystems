# crytposystems
RSA and ElGamal implementation using [Charm-Crypto](https://jhuisi.github.io/charm/)
* RSA Cryptosystem (Based on Factorization Problem)
1.   Select large primes p, q such that p≠ q
2.   Calculate n = p*q and Ø(n) = (p-1)*(q-1)
3.   Select b such that gcd(Ø(n),b) = 1 and 1<b< Ø(n)
4.   Compute d such that bd ≅ 1(mod Ø(n))
5.   Public key (n, b) and private key (d,n)
6.   Encryption for message m: c = Ek(m) = mb(mod n)
7.   Decryption for cipher c: Dk(c) = cd(mod n)

* ElGamal Cryptosystem (Based on Discrete Logarithm)
1.   p:Prime, (Zp*, . ) and α ∈ Zp* primitive element.
2.   {(p, α, a, ß): αa ≅ ß (mod p)}
3.   Public: (p, α, ß) and Private: a
4.   Encryption for message m: Select random number r ∈ Zp-1* 
       c = Ek(m) = (y1,y2) where y1 = αr (mod p) and y2 = m. ßr(mod p)
5.   Decryption for cipher c: Dk(c) = y2.(y1a)-1
