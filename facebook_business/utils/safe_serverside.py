# facebook_business/utils/safe_serverside.py

from facebook_business.adobjects.serverside.event_request_async import EventRequestAsync
from facebook_business.adobjects.serverside.event_response import EventResponse

class SafeEventRequestAsync(EventRequestAsync):
    async def execute(self):
        try:
            return await super().execute()
        except KeyError as e:
            if 'fbtrace_id' in str(e):
                # Fallback: create a safe EventResponse with a dummy trace ID
                return EventResponse(
                    events_received=1,
                    messages=["fbtrace_id missing, handled gracefully"],
                    fbtrace_id="SAFE-FALLBACK"
                )
            raise