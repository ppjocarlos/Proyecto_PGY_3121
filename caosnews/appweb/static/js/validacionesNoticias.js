function validarSeccion(seccion){

    if (seccion == ""){
        return false;
    }
    return true;
}

function validarCampoVacio(texto){

    if (texto.length > 2){
        return true;
    }
    return false;
}

function validarLargoRut(rut){

    if (rut.length >= 9 && rut.length <= 10 ){
        return true;
    }
    return false;
}

