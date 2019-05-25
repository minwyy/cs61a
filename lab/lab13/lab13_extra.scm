; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
  (cond
   ((null? s) nil)
   ((not (pair? s)) (cons s nil))    
   (else (if (pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))) (cons (car s) (nodots (cdr s))) ))
)
)

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? curr seen-so-far) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (cond 
  	((null? s) #f)
  	 ((eq? lst (car s)) #t)
  	 (else (contains? lst (cdr s)))
)
)


; Q8
(define-macro (switch expr cases)
    (list 'cond 
    	((list '= expr (car (car cases))) (cdr (car cases)))
    	(switch expr (cdr cases))
)
)


; (define-macro (switch expr cases)
;               (let ((val (eval expr)))
;                    (cons 'cond
;                          (map (lambda (case)
;                                       (cons (eq? val (car case)) (cdr case))
;                               )
;                               cases
;                          )
;                    )
;               )
; )