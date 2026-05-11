# Stored Procedure: `sp_KSTC_PR_CheckChietKhauThucTreo_PhanBo_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-29 13:59:49.687000
- **Ngày sửa cuối**: 2021-10-29 13:59:49.687000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[sp_KSTC_PR_CheckChietKhauThucTreo_PhanBo_v2]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select 'NGUON'[NoiCheck], B.* ,A.*
from(
  select  id,ChietKhau as ChietKhauThucTreo,contract_detail_id
  from [asdag2].thuctreo.dbo.thuctreo_pr
  where Deleted_Status = 0
)A
inner join
(
  select hd.contract_number,hdct.id HopDongChiTietID,hdct.percent_discount_total as ChietKhauhd, hdct.Last_Modified_At 
  from [ASDAG2].contract.dbo.contracts hd
  inner join [ASDAG2].contract.dbo.contract_details hdct
  on hd.id=hdct.contract_id
  where 1=1
  and hdct.Deleted_Status=0
  and hd.contract_year >=2020
)B
on A.contract_detail_id = B.HopDongChiTietID
where not A.ChietKhauThucTreo =B.ChietKhauhd

select 'DICH'[NoiCheck],B.* ,A.*
from(
  select  ChietKhau as ChietKhauThucTreo,HopDongChiTietREF
  from ThucChayHopDongChiTietPR
  where DeletedStatus = 0
)A
inner join
(
  select hd.SoHopDong,hd.HopDongID,hdct.HopDongChiTietID,hdct.ChietKhau as ChietKhauhd, hdct.LastModifiedAt 
  from HopDong hd
  inner join HopDongChiTiet hdct
  on hd.HopDongID=hdct.HopDongFK
  where 1=1
  and hdct.DeletedStatus=0
  and hd.Nam >=2020
)B
on A.HopDongChiTietREF = B.HopDongChiTietID
where not A.ChietKhauThucTreo =B.ChietKhauhd
END

```
