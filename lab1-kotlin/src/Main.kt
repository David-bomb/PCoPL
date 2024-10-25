import kotlin.math.sqrt

fun checkArr(args: MutableList<String?>): Boolean { // Проверка списка коэф.: кол-во, числа ли это
    var DotCounter : Int
    if (args.size != 3){
        return false
    }
    for (arg in args) {
        DotCounter = 0
        if (arg != null) {
            if (arg.length == 0){
                return false
            }
            for (j: Int in 0..(arg.length - 1)) {
                if (j == 0) {
                    if (!((arg[j] in '0'..'9') or (arg[j] == '-'))) {
                        return false
                    }
                } else {
                    if (!((arg[j] in '0'..'9') or (arg[j] == '.'))) {
                        return false
                    }
                    if (arg[j] == '.') {
                        DotCounter += 1
                        if (DotCounter > 1) {
                            return false
                        }
                    }
                }
            }
        }
    }
    return true
}

fun enter_coefs(console: Array<String>? = null): MutableList<String?> { // Ввод коэф. Если есть ввод с консоли, то принимаем из консоли
    if (console != null){
        var cont : MutableList<String?> = mutableListOf()
        for (i in 0 .. (console.size - 1)){
            cont.add(i, console[i])
        }
        if (checkArr(cont)) {
            return cont
        }
        return enter_coefs()
    }
    print("Введите A: ")
    var A: String? = readLine()
    print("Введите B: ")
    var B: String? = readLine()
    print("Введите C: ")
    var C: String? = readLine()
    var args = mutableListOf<String?>(A, B, C)
    // var test = listOf(A, B, C)
    if (checkArr(args)) {
        return args
    }
    return enter_coefs()
}

fun strToDbl(coefs : MutableList<String?>) : MutableList<Double>{ // Конвертация списка String? в список Double
    var new_coefs = mutableListOf<Double>()
    for (i in 0 .. (coefs.size - 1)){
        new_coefs.add(i, (coefs[i].toString().toDouble()))
    }
    return new_coefs
}

fun findDesicion(coefs: MutableList<Double>) { // Подсчет корней
    val D : Double = coefs[1]*coefs[1] - 4*coefs[0]*coefs[2]
    val x1 : Double = (-coefs[1] + sqrt(D))/(2*coefs[0])
    val x2 : Double = (-coefs[1] - sqrt(D))/(2*coefs[0])
    when{
        D > 0 -> {
            val x1 : Double = (-coefs[1] + sqrt(D))/(2*coefs[0])
            val x2 : Double = (-coefs[1] - sqrt(D))/(2*coefs[0])
            println("Корни: " + x1.toString() + " " + x2.toString())}

        D == 0.0 -> {
            val x : Double = (-coefs[1] + sqrt(D))/(2*coefs[0])
            println("Корень: " + x.toString())}
        D < 0 -> {
            println("Корней нет.")}
    }
}

fun main(args: Array<String>?) {
    var coefs : MutableList<Double> = strToDbl(enter_coefs(args))
    findDesicion(coefs)
}