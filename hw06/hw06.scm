(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((> num 0) 1)
        ((= num 0) 0)
        (else -1))
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  '(print y)
  (if (= y 1) x
  (cond ((even? y) (square (pow x (/ y 2))))
       ((odd? y) (* x (square (pow x (/ (- y 1) 2)))))))
)

