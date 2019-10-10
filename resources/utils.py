import datetime
import dateutil.rrule


def check_import():
    print("Imported!")
    return 0

def rename_category_for_flattening(category, category_parent):
    """
    #TODO: documentation
    """
    return category_parent + "_" + category.lower().replace(" ", "_")

def sequential_months(dates):
    """
    #TODO: documentation
    """
    strt_dt = datetime.datetime.strptime(min(dates), "%Y%m")
    end_dt = datetime.datetime.strptime(max(dates), "%Y%m")

    n_months = len([dt for dt in dateutil.rrule.rrule(dateutil.rrule.MONTHLY, dtstart=strt_dt, until=end_dt)])
    return n_months == len(dates)