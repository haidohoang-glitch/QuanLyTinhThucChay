# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_PR_Log`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-04 16:18:12.470000
- **Ngày sửa cuối**: 2025-10-24 14:32:23.923000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_PR_Log]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_PR_Log]
AS
BEGIN
    DECLARE @NgayThucHien DATETIME;
    DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = '''',
            @LoaiThucTreo_chiphi NVARCHAR(50) = N'';
    SET @NgayThucHien = ISNULL(
                        (
                            SELECT MAX(dchdct.[ThoiGianLog])
                            FROM dbo.[ThucChayHopDongChiTietPRLog] dchdct

                        ),
                        '2019-01-01'
                              );

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id),'')

    SET @NgayThucHien = DATEADD(HOUR, -1, @NgayThucHien);
    --SET @NgayThucHien = '2009-01-01'

    PRINT @NgayThucHien;


	CREATE TABLE #ThucChayHopDongChiTietPRLog(
		[ThucChayHopDongChiTietPRREF] [int] NOT NULL,
		[HopDongREF] [bigint] NOT NULL,
		[HopDongChiTietREF] [bigint] NULL,
		[DmWebsiteREF] [int] NULL,
		[TenWebsite] [nvarchar](200) NULL,
		[DmChuyenMucREF] [int] NULL,
		[TenChuyenMuc] [nvarchar](200) NULL,
		[TieuDiem] [int] NULL,
		[DmNhanHangREF] [nvarchar](200) NULL,
		[NhanHang] [nvarchar](200) NULL,
		[KhuyenMai] [int] NULL,
		[GiaTien] [bigint] NULL,
		[ThoiGianBatDau] [datetime] NULL,
		[Link] [nvarchar](2000) NULL,
		[GhiChu] [nvarchar](2000) NULL,
		[DmHinhThucQuangCaoREF] [int] NULL,
		[TenHinhThucQuangCao] [nvarchar](200) NULL,
		[ThoiGianLog] [datetime] NULL,
		[NguoiLog] [nvarchar](200) NULL,
		[LoaiLog] [int] NULL,
		[CreatedBy] [nvarchar](200) NULL,
		[CreatedAt] [datetime] NULL,
		[LastModifiedBy] [nvarchar](200) NULL,
		[LastModifiedAt] [datetime] NULL,
		[DeletedStatus] [int] NULL,
		[PrintStatus] [int] NULL,
		[RecordStatus] [int] NULL,
		[SoLuong] [int] NULL,
		[ChietKhau] float)


	SET @SQL =
	'INSERT INTO #ThucChayHopDongChiTietPRLog
			   ([ThucChayHopDongChiTietPRREF]
			   ,[HopDongREF]
			   ,[HopDongChiTietREF]
			   ,[DmWebsiteREF]
			   ,[TenWebsite]
			   ,[DmChuyenMucREF]
			   ,[TenChuyenMuc]
			   ,[TieuDiem]
			   ,[DmNhanHangREF]
			   ,[NhanHang]
			   ,[KhuyenMai]
			   ,[GiaTien]
			   ,[ThoiGianBatDau]
			   ,[Link]
			   ,[GhiChu]
			   ,[DmHinhThucQuangCaoREF]
			   ,[TenHinhThucQuangCao]
			   ,[ThoiGianLog]
			   ,[NguoiLog]
			   ,[LoaiLog]
			   ,[CreatedBy]
			   ,[CreatedAt]
			   ,[LastModifiedBy]
			   ,[LastModifiedAt]
			   ,[DeletedStatus]
			   ,[PrintStatus]
			   ,[RecordStatus]
			   ,[SoLuong]
			   ,[ChietKhau]) '
	SET @SQL +=
			' SELECT [id]
      ,[Contract_Id]
	  ,[Contract_Detail_Id]
	  ,[Website_id]
	  ,[Ten_Website]
	  ,0 Chuyenmucid
	  ,[TenChuyenMuc]
	  ,[TieuDiem]
	  ,[NhanHang_Id]
	  ,[TenNhanHang]
      ,[KhuyenMai]
	  ,[DonGia]
	  ,[ThoiGianBatDau]
	  ,[Link]
      ,LEFT([GhiChu],150) ghichu
	  ,[Product_Formality_Id]
	  ,'''' as TenHTQC
      ,[SysEndTime] as thoigianlog
	  ,'''' as nguolog
	  ,0 as loailog
	  ,[Created_By]
      ,[Created_At]
      ,[Last_Modified_By]
      ,[Last_Modified_At]
	  ,[Deleted_Status]
	  ,0 as PrintStatus
	  ,0 [RecordStatus]
	  ,[SoLuong]
      ,[ChietKhau]
	 FROM ' + @server_id + '.' + @database + '.[dbo].[ThucTreo_PRHistory] tt
		WHERE 1=1 
		AND tt.[SysEndTime] > ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

		PRINT @SQL
		EXEC(@SQL)
		--select * from #ThucChayHopDongChiTietLog

	INSERT INTO [dbo].[ThucChayHopDongChiTietPRLog]
           ([ThucChayHopDongChiTietPRREF]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[DmChuyenMucREF]
           ,[TenChuyenMuc]
           ,[TieuDiem]
           ,[DmNhanHangREF]
           ,[NhanHang]
           ,[KhuyenMai]
           ,[GiaTien]
           ,[ThoiGianBatDau]
           ,[Link]
           ,[GhiChu]
           ,[DmHinhThucQuangCaoREF]
           ,[TenHinhThucQuangCao]
           ,[ThoiGianLog]
           ,[NguoiLog]
           ,[LoaiLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
           ,[SoLuong]
           ,[ChietKhau])
  
 
	SELECT [ThucChayHopDongChiTietPRREF]
      ,[HopDongREF]
      ,[HopDongChiTietREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[TieuDiem]
      ,[DmNhanHangREF]
      ,[NhanHang]
      ,[KhuyenMai]
      ,[GiaTien]
      ,[ThoiGianBatDau]
      ,[Link]
      ,[GhiChu]
      ,[DmHinhThucQuangCaoREF]
      ,[TenHinhThucQuangCao]
      ,[ThoiGianLog]
      ,[NguoiLog]
      ,[LoaiLog]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[LastModifiedAt]
      ,[DeletedStatus]
      ,[PrintStatus]
      ,[RecordStatus]
      ,[SoLuong]
      ,[ChietKhau]
	FROM #ThucChayHopDongChiTietPRLog

    DROP TABLE #ThucChayHopDongChiTietPRLog

END;


```
