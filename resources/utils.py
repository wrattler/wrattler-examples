import datetime
import dateutil.rrule

def rename_category_for_flattening(category, category_parent=""):
    """
    Tidy name of passed category.
    
    :param category: string to be renamed (namely, a category of crime)
    :param category_parent: optional string to insert at the beginning of the string (in addition to other edits)
    :return: new string name for category passed
    """
    if category_parent == "":
        return category.lower().replace(" ", "_").replace("/", "").replace("(", "").replace(")", "").replace(",", "").replace(";", "_").replace("-", "")
    
    return category_parent + "_" + category.lower().replace(" ", "_").replace("/", "").replace("(", "").replace(")", "").replace(",", "").replace(";", "").replace("-", "")

def sequential_months(dates):
    """
    Check whether list of given dates is sequential. 
    
    :param dates: list of string representations of dates in format "%Y%m" (e.g. "201810" -> 2018, Oct)
    :return: True if sequential
    """
    strt_dt = datetime.datetime.strptime(min(dates), "%Y%m")
    end_dt = datetime.datetime.strptime(max(dates), "%Y%m")

    n_months = len([dt for dt in dateutil.rrule.rrule(dateutil.rrule.MONTHLY, dtstart=strt_dt, until=end_dt)])
    return n_months == len(dates)