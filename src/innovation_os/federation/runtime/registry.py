class TenantRegistry:


    def __init__(self):

        self.tenants = {}



    def register(
        self,
        tenant
    ):

        self.tenants[
            tenant.tenant_id
        ] = tenant

        return tenant



    def get(
        self,
        tenant_id
    ):

        return self.tenants.get(
            tenant_id
        )
