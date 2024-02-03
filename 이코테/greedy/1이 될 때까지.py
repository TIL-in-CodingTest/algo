{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "n, k = map(int, input().split())\n",
    "result = 0\n",
    "\n",
    "while True :\n",
    "    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기\n",
    "    target = (n // k) * k\n",
    "    result += (n - target)\n",
    "    if n<k:\n",
    "        break\n",
    "    result += 1\n",
    "    n // k\n",
    "result += (n-1)\n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
