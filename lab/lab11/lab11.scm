


(define-macro (def func bindings body)
    (list 'define (cons func bindings) body)
)