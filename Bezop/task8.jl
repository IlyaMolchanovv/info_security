#task8

function factor_ferma(n::BigInt, k)
  m = isqrt(n)  # Используем функцию `isqrt` для извлечения корня нацело
  m = m + (m % 2 - 1)  # Делитель должен быть нечетным

  for i in m:2:(m + k)
      
      if n % i == 0
          println(i)
          break
      end
  end

  println("Поиск завершен")
end


k = 10000000


n = 745080457478324832794684995083661325718066869026770951749204860652467077560034632695487788816842443

factor_ferma(n, k)
