# Stored Procedure: `ThucChayDaTinhViewPlusForDomain_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-05-13 18:13:44.240000
- **Ngày sửa cuối**: 2015-06-25 17:40:33.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		Luong Van Ly
-- Create date: 04/22/2015
-- Description:	Delete ThucChayDaTinhViewPlusForDomainForDomain 
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhViewPlusForDomain_Delete]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @DmSanPhamREF INT
AS 
    BEGIN	
		
        DELETE  dbo.ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, @StartDate)
                AND DmSanPhamREF = @DmSanPhamREF                        
    
        DELETE  dbo.ThucChayDaTinhViewPlusForDomainForDomain
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, @StartDate)
                AND DmSanPhamREF = @DmSanPhamREF
    END

```
