# AUTO GENERATED FILE - DO NOT EDIT

''MessageLog <- function(id=NULL, log=NULL, trigServLogUpdate=NULL) {
    
    props <- list(id=id, log=log, trigServLogUpdate=trigServLogUpdate)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MessageLog',
        namespace = 'bindingtests',
        propNames = c('id', 'log', 'trigServLogUpdate'),
        package = 'bindingtests'
        )

    structure(component, class = c('dash_component', 'list'))
}
