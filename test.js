function countPrimes(n) {
    if (n < 2) {
        return { count: 0, primes: [] };
    }

    const isPrime = Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;

    for (let i = 2; i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    const primeNumbers = [];
    isPrime.forEach((prime, index) => {
        if (prime) {
            primeNumbers.push(index);
        }
    });

    return { count: primeNumbers.length, primes: primeNumbers };
}

const n = 18;
const { count, primes } = countPrimes(n);
console.log(`${n} тоо хүртэл анхны тоо ${count}: ${primes}`);
