# **Issue**

## **Description**

Using the python sdk I'm trying to get insights of ad account on ad level by using around 10-20 fields for a single day's data by breaking it down to dma.

API gives the error that the amount of data which you are asking is to much

- Response
{
  "error": {
    "code": 1,
    "message": "Please reduce the amount of data you're asking for, then retry your request"
  }
}



- Query Parameters
  {
    "fields": "ad_id,ad_name,impressions,reach,spend",
    "filtering": "[{\"field\": \"impressions\",\"operator\":\"GREATER_THAN\", \"value\": 50}]",
    "breakdowns": "dma",
    "time_range": "{\"since\":\"2021-05-10\",\"until\":\"2021-05-10\"}",
    "time_increment": "1",
    "limit": "1000",
    "level": "ad"
  }
  
  
  
  ## **Let me know how to resolve this issue**
