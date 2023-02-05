PSO, Partikül Kuşağı Optimizasyonu olarak adlandırılır. Bu, kuşlar ve diğer hayvanların bir kümede veya kuşağında sosyal davranışlarından ilham alan bir metaheuristik
(Metaheuristik, bir problemi çözmek için uygulanabilecek bir optimizasyon yöntemi olarak tanımlanabilir. Bu yöntemler, matematiksel modelleme veya doğrusal programlama
gibi doğrusal yaklaşımlardan farklı olarak, bir heuristic (tahmin yapma) yoluyla çalışır. Metaheuristik yöntemler, en iyi sonucu bulmak için birçok aday çözümü denemeyi
ve bu çözümleri iteratif olarak güncellemeyi içerebilir.) optimizasyon algoritmasıdır. PSO, bir grup parçacığın hareketini simüle ederek çok boyutlu arama uzayının 
global optimumunu bulmak için kullanılır. Her parçacık, sorunun bir aday çözümünü temsil eder ve pozisyonunu kuşağın diğer parçacıklarının deneyimlerine ve kendi 
deneyimine göre günceller.
PSO algoritmasının genel bir çerçevesi şu şekildedir:

•	Parçacıkların nüfusunu başlatın: Her parçacık, arama uzayındaki rastgele bir pozisyon ve hız atanır.
•	Her parçacığın uygunluğunu değerlendirin: Her parçacığın şu anki pozisyonuna dayanarak hedef fonksiyon değerini hesaplayın.
•	Küresel en iyi pozisyonu güncelleyin: En iyi hedef fonksiyon değerine sahip parçacığı belirleyin ve onu saklayın.
